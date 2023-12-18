#lang racket

;; CIS352
;; Project 4: A church-compiler: Scheme -> Lambda-calculus
;; see README.md

(provide church-compile
         ; provided conversions:
         church->nat
         church->bool
         church->listof)

;; Input language:
;
; e ::= (letrec ([x (lambda (x ...) e)]) e)    
;     | (let ([x e] ...) e)  
;     | (let* ([x e] ...) e)
;     | (lambda (x ...) e)
;     | (e e ...)    
;     | x  
;     | (and e ...) | (or e ...)
;     | (if e e e)
;     | (prim e) | (prim e e)
;     | datum
; datum ::= nat | (quote ()) | #t | #f 
; nat ::= 0 | 1 | 2 | ... 
; x is a symbol
; prim is a primitive operation in list prims
; The following are *extra credit*: -, =, sub1  
(define prims '(+ * - = add1 sub1 cons car cdr null? not zero?))

; This input language has semantics identical to Scheme / Racket, except:
;   + You will not be provided code that yields any kind of error in Racket
;   + You do not need to treat non-boolean values as #t at if, and, or forms
;   + primitive operations are either strictly unary (add1 sub1 null? zero? not car cdr), 
;                                           or binary (+ - * = cons)
;   + There will be no variadic functions or applications---but any fixed arity is allowed

;; Output language (you must produce a quoted expression satisfying this grammar):
;;
;; e ::= (lambda (x) e)
;;     | (e e)
;;     | x
;;
;; also as interpreted by Racket

;; Decoding to Racket

;; Using the following decoding functions:

; A church-encoded nat is a function taking an f, and x, returning (f^n x)
(define (church->nat c-nat)
  ((c-nat add1) 0))

; A church-encoded bool is a function taking a true-thunk and false-thunk,
;   returning (true-thunk) when true, and (false-thunk) when false
(define (church->bool c-bool)
  ((c-bool (lambda (_) #t)) (lambda (_) #f)))

; A church-encoded cons-cell is a function taking a when-cons callback, and a when-null callback (thunk),
;   returning when-cons applied on the car and cdr elements
; A church-encoded cons-cell is a function taking a when-cons callback, and a when-null callback (thunk),
;   returning the when-null thunk, applied on a dummy value (arbitrary value that will be thrown away)
(define ((church->listof T) c-lst)
  ; when it's a pair, convert the element with T, and the tail with (church->listof T)
  ((c-lst (lambda (a) (lambda (b) (cons (T a) ((church->listof T) b)))))
   ; when it's null, return Racket's null
   (lambda (_) '())))


;; Write your church-compiling code below:

;; (churchify e) churchify recursively walks over e and converts each
;; expression in the input language (defined above, see "input
;; language") to an equivalent (when converted back via each
;; church->XYZ) expression in the lambda calculus (defined above, see
;; "output language")
;;
;; note: both the input and output will be quoted expressions--the
;; test scripts will use Racket's `eval` to turn them into Racket
;; lambdas.
(define (churchify e) 
  ;; you may modify the match statement if helpful--but this is
  ;; roughly what the reference solution uses.
  (define ycomb `((lambda (u) (u u)) (lambda (y) (lambda (mk) (mk (lambda (x) (((y y) mk) x))))))) 
  (match e  
         [`(letrec ([,f (lambda (,x ...) ,e-body)]) ,let-body)
          (churchify `(let ([,f (,ycomb (lambda (,f) (lambda (,@x) ,e-body)))]) ,let-body))]    
         [`(let () ,e1)
          `(churchify e1)]    
         [`(let ([,xs ,e0s] ...) ,e1)
          (churchify `((lambda ,xs ,e1) . ,e0s))]    
         [`(let* () ,e1)
          `(churchify e1)]    
         [`(let* ,args ,xs)
          (churchify (foldr
                      (lambda (x acc)
                        `((lambda (,(first x)) ,acc) ,(first (rest x))))
                      xs
                      args))]   
         [`(lambda () ,e0)
          `(lambda (_) ,(churchify e0))]    
         [`(lambda (,x) ,e0)
          `(lambda (,x) ,(churchify e0))]    
         [`(lambda (,x . ,rest) ,e0)
          `(lambda (,x) ,(churchify `(lambda ,rest ,e0)))] 
         [`(and)
          (churchify '#t)]    
         [`(and ,e0 ,rest ...)
          (churchify `(if ,e0 (and ,@rest)) #f)]    
         [`(or)
          (churchify '#f)]    
         [`(or ,e0 ,rest ...)
          (churchify `(if ,e0 #t (or ,@rest)))]    
         [`(if ,e0 ,e1 ,e2)
          (churchify `(,e0 (lambda () ,e1) (lambda () ,e2)))]    
         ; Variables
         [(? symbol? x) x]   
         ; Datums
         [(? natural? nat)
          (define (gen nat)
            (if (= 0 nat) 'x `(f ,(gen (- nat 1)))))
          (churchify `(lambda (f) (lambda (x) ,(gen nat))))]   
         [''()
          (churchify `(lambda (when-cons) (lambda (when-null) (when-null))))]    
         [#t
          '(lambda (x) (lambda (y) (x (lambda (x) x))))]
         [#f
          (churchify '(lambda (t f) (f)))]   
         ; Untagged application
         [`(,fun)
          (churchify `(,fun (lambda (_) _)))]
         [`(,fun ,arg)
          `(,(churchify fun) ,(churchify arg))]
         [`(,fun ,arg . ,rest)
          (churchify `((,fun ,arg) . ,rest))]))


; Takes a whole program in the input language, and converts it into an equivalent program in lambda-calc
(define (church-compile program)
  ; Define primitive operations and needed helpers using a top-level let form?
  (define ycomb `((lambda (u) (u u)) (lambda (y) (lambda (mk) (mk (lambda (x) (((y y) mk) x)))))))
  (define cnull? `(lambda (p) (p (lambda (a b) #f) (lambda () #t))))
  (define plus `(lambda (n0 n1) (lambda (f x) ((n1 f) ((n0 f) x)))))
  (define succ '(lambda (n) (lambda (f) (lambda (z) (((n (lambda (g) (lambda (h) (h (g f))))) (lambda (u) z)) (lambda (u) u))))))
  (define sub `(lambda (n) (lambda (m) ((m ,succ) n))))
  (define times `(lambda (n) (lambda (m) (lambda (f) (lambda (x) ((m (n f)) x))))))
  (define cadd1 `(lambda (n) (lambda (f x) (f ((n f) x)))))
  (define ccons `(lambda (a) (lambda (b) (lambda (when-cons) (lambda (when-empty) (when-cons a b))))))
  (define cnot `(lambda (x) (lambda (t) (lambda (f) (x f t)))))
  (define czero? `(lambda (n) (n (lambda (x) #f) #t)))
  
  (churchify
   `(let ([ycomb ,ycomb]
          [null? ,cnull?]
          [+ ,plus]
          [- ,sub]
          [* ,times]
          [add1 ,cadd1]
          [cons ,ccons]
          [not ,cnot]
          [zero? ,czero?]
          )
          ,program)))

