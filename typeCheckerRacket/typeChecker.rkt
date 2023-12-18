#lang racket

;; Tuesday, Apr 25, 2022
;; Type Checking
;; 
;; In this project, we will check fully-annotated STLC terms. In the
;; next project we will look at synthesis, but it will not be a graded
;; part of the assignment.

;; We will build a type system based on the Simply-Typed λ-calculus
;; (STLC). STLC contains reduction rules for 

(provide (all-defined-out))

;;
;; Type Checking
;;

;; Primitive literals
(define bool-lit? boolean?)
(define int-lit? integer?)
 
;; Expressions are ifarith, with several special builtins
(define (expr? e)
  (match e
    ;; Variables
    [(? symbol? x) #t]
    ;; Literals
    [(? bool-lit? b) #t]
    [(? int-lit? i) #t]
    ;; Applications
    [`(,(? expr? e0) ,(? expr? e1)) #t]
    ;; Annotated expressions
    [`(,(? expr? e) : ,(? type? t)) #t]
    ;; Anotated lambdas
    [`(lambda (,(? symbol? x) : ,(? type? t)) ,(? expr? e)) #t]))

;; Types for STLC
(define (type? t)
  (match t
    ;; Base types: int and bool
    ['int #t]
    ['bool #t]
    ;; Arrow types: t0 -> t1
    [`(,(? type? t0) -> ,(? type? t1)) #t]
    [_ #f]))

;; Synthesize a type for e in the environment env
;; Returns a type
;;
;; Note: synthesis in this setting is *syntax directed*, because
;; the type of the lambda's argument is forced to be annotated.
;; Annotations on arguments are the primary source of nondeterminism
;; when we think about reconstructing a type's proof

;;
;; TODO (Part 1)
;;
(define (synthesize-type env e)
  (match e
    ;; Literals
    [(? integer? i) 'int]
    [(? boolean? b) 'bool]
    ;; Look up a type variable in an environment
    [(? symbol? x) (hash-ref env x)]
    ;; Lambda w/ annotation
    [`(lambda (,x : ,A) ,e)
     (define t0 A)
     (define t1 (synthesize-type (hash-set env x A) e))
     `(,t0 -> ,t1)]
    ;; Arbitrary expression
    [`(,e : ,t)
     (if (equal? t (synthesize-type env e))
         (synthesize-type env e)
         (error (format "bad type assertion" (synthesize-type env e) t)))]
    ;; Application
    [`(,e1 ,e2)
     (match (synthesize-type env e1)
       [`(,T0 -> ,T1)
	(define T2 (synthesize-type env e2))
        (if (equal? T0 T2)
            T1
            (error "error"))]
       [_ (error "applying something that is *not* an arrow type")])]))

;; To synthesize an STLC type, synthesize a type with a starting environment
(define (synthesize-stlc-type e)
  (synthesize-type (hash '+ '(int -> (int -> int))
                         'is-zero? '(int -> bool))
                   e))

;; Tests 1: public-synthesize
#;(synthesize-stlc-type '((lambda (x : int) x) 23))
#;(synthesize-stlc-type '(lambda (x : int) (lambda (y : bool) (lambda (z : int) x))))
#;(synthesize-stlc-type '(lambda (x : (int -> int)) (lambda (y : bool) (lambda (z : int) (x (13 : int))))))

;; To type check: synthesize then match

;; Check that, in an environment env, e's type is t
;; Returns a bool
;;
;;
(define (check-stlc-type e t)
  (with-handlers ([exn:fail? (lambda (exn) #f)])
    (if (equal? (synthesize-stlc-type e) t)
        #t 
        #f))) 

;; Tests 2: public-typecheck
#;(check-stlc-type '((lambda (x : int) x) 23) 'int)
#;(check-stlc-type '(lambda (x : int) (lambda (y : bool) (lambda (z : int) x)))
                 '(int -> (bool -> (int -> int))))
#;(check-stlc-type
 '(lambda (x : (int -> int)) (lambda (y : bool) (lambda (z : int) (x (13 : int)))))
 '((int -> int) -> (bool -> (int -> int))))


;;
;;

;; Erase types: transform to Racket code
(define (erase-types e)
  (match e
    [`((+ ,e0) ,e1) '(+ ,(erase-types e0) ,(erase-types e1))]
    [`(lambda (,x : ,t) ,e) '(lambda(,x) ,(erase-types e))]
    [(? symbol? x) x]
    [(? bool-lit? b) b]
    [(? int-lit? i) i]
    [`(,e : ,t) (erase-types e)]
    [`(,e0 ,e1) '(,(erase-types e0) ,(erase-types e1))]))

;; returns either 'type-error or the expression
;; Converting STLC to Racket means first (a) run the typechecker and
;; (b) then erase the types

(define (stlc->racket e)
  (with-handlers ([exn:fail? (lambda (exn) 'type-error)]) 
    (begin
      (synthesize-stlc-type e)
      (erase-types e))))
