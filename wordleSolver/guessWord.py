with open("wordlist.txt", "r") as f:
    copy = sorted(word.strip(",")
for line in f for word in line.split())



def guessWord(word):
    first_guess = "salet"
    letterdict = {}
    strlist = ""
    bestscore = 0
    bestword = ""
    guesses = 1
    letterinword = 0
    wordlist = copy.copy()
    newwordlist = []

    for x in range(5):
        if first_guess[x] == word[x]:
            letterinword += 1
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] != item[x]:
                    wordlist[i] = "0"
        elif first_guess[x] in word:
            letterinword += 1
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] == item[x]:
                    wordlist[i] = "0"
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] not in item:
                    wordlist[i] = "0"
        else:
            for i in range(len(wordlist)):
                item = wordlist[i]
                if len(item) > 1 and first_guess[x] in item:
                    wordlist[i] = "0"
    print(first_guess + ", " + str(len(wordlist)) + " possible guesses before this guess")
    for i in wordlist:
        if i != "0":
            newwordlist.append(i)

    for i in newwordlist:
        strlist = strlist + i
    for item in strlist:
        if item in letterdict:
            letterdict[item] += 1
        else:
            letterdict[item] = 1

    for z in newwordlist:
        currword = list(z)
        currscore = 0
        for y in range(len(currword)):
            if currword[y] != currword[y-1]:
                currscore += letterdict[currword[y]]
            if currword[y] in "rioncbpf":
                currscore += 60
            if currword.count(currword[y]) <= 1:
                currscore += 10000

        if currscore > bestscore:
            bestscore = currscore
            bestword = z
        if letterinword <= 1:
            bestword = "choir"
    print(bestword + ", " + str(len(newwordlist)) + " possible guesses before this guess")
    guesses += 1
    while bestword != word:
        wordlist = newwordlist
        looplist = []
        letterdict = {}
        strlist = ""
        currguess = bestword
        for x in range(5):
            if currguess[x] == word[x]:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] != item[x]:
                        wordlist[i] = "0"
            elif currguess[x] in word:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] == item[x]:
                        wordlist[i] = "0"
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] not in item:
                        wordlist[i] = "0"
            else:
                for i in range(len(wordlist)):
                    item = wordlist[i]
                    if len(item) > 1 and currguess[x] in item:
                        wordlist[i] = "0"

        for i in wordlist:
            if i != "0":
                looplist.append(i)

        bestscore = 0
        bestword = ""

        for i in looplist:
            strlist = strlist + i
        for item in strlist:
            if item in letterdict:
                letterdict[item] += 1
            else:
                letterdict[item] = 1

        for z in looplist:
            currword = list(z)
            currscore = 0
            for y in range(len(currword)):
                if currword[y] != currword[y - 1]:
                    currscore += letterdict[currword[y]]
                if currword[y] not in "qzj":
                    currscore += 50
                if currword.count(currword[y]) <= 1:
                    currscore += 10
            if currscore > bestscore:
                bestscore = currscore
                bestword = z
        guesses += 1
        print(bestword + ", " + str(len(looplist)) +" possible guesses before this guess")
    print(str(guesses) + " guesses")

guessWord("canny")
