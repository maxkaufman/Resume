import random

h1 = 9
h2 = 7
h3 = 11
d1 = 3
d2 = 5
d3 = 7

def exploreOnly():
    totalhappiness = 0
    caf1 = 0
    caf2 = 0
    caf3 = 0
    while caf1 < 100:
        totalhappiness += random.normalvariate(h1,d1)
        caf1 += 1
    while caf2 < 100:
        totalhappiness += random.normalvariate(h2,d2)
        caf2 += 1
    while caf3 < 100:
        totalhappiness += random.normalvariate(h3,d3)
        caf3 += 1
    return totalhappiness

def exploitOnly():
    totalH = 0
    C1 = random.normalvariate(h1,d1)
    totalH += C1
    C2 = random.normalvariate(h2,d2)
    totalH += C2
    C3 = random.normalvariate(h3,d3)
    totalH += C3
    days = 3
    if(C1 > C2) & (C1 > C3):
        while(days < 300):
            C1 = random.normalvariate(h1, d1)
            totalH += C1
            days +=1
    elif (C2 > C1) & (C2 > C3):
        while (days < 300):
            C2 = random.normalvariate(h2, d2)
            totalH += C2
            days += 1
    else:
        while (days < 300):
            C3 = random.normalvariate(h3, d3)
            totalH += C3
            days += 1
    return totalH

def eGreedy(e):
    e = e/100
    caf1happiness = 0
    caf2happiness = 0
    caf3happiness = 0
    caf1count = 0
    caf2count = 0
    caf3count = 0
    totalhappiness = 0
    mealcount = 3
    mealhappiness = random.normalvariate(h1, d1)
    totalhappiness += mealhappiness
    caf1happiness += mealhappiness
    caf1count += 1
    mealhappiness = random.normalvariate(h2, d2)
    totalhappiness += mealhappiness
    caf2happiness += mealhappiness
    caf2count += 1
    mealhappiness = random.normalvariate(h3, d3)
    totalhappiness += mealhappiness
    caf3happiness += mealhappiness
    caf3count += 1
    while mealcount < 300:
        caf1avg = caf1happiness/caf1count
        caf2avg = caf2happiness/caf2count
        caf3avg = caf3happiness/caf3count
        if random.random() > (1-e):
            whichcaf = random.randint(1,3)
            if whichcaf == 1:
                mealhappiness = random.normalvariate(h1, d1)
                totalhappiness += mealhappiness
                caf1happiness += mealhappiness
                caf1count += 1
            elif whichcaf == 2:
                mealhappiness = random.normalvariate(h2, d2)
                totalhappiness += mealhappiness
                caf2happiness += mealhappiness
                caf2count += 1
            elif whichcaf == 3:
                mealhappiness = random.normalvariate(h3, d3)
                totalhappiness += mealhappiness
                caf3happiness += mealhappiness
                caf3count += 1
        else:
            if caf1avg > caf2avg and caf1avg > caf3avg:
                mealhappiness = random.normalvariate(h1, d1)
                totalhappiness += mealhappiness
                caf1happiness += mealhappiness
                caf1count += 1
            elif caf2avg > caf1avg and caf2avg > caf3avg:
                mealhappiness = random.normalvariate(h2, d2)
                totalhappiness += mealhappiness
                caf2happiness += mealhappiness
                caf2count += 1
            elif caf3avg > caf1avg and caf3avg > caf2avg:
                mealhappiness = random.normalvariate(h3, d3)
                totalhappiness += mealhappiness
                caf3happiness += mealhappiness
                caf3count += 1
        mealcount += 1
    return totalhappiness



def simulation(e,t):
    exploitcount = 0
    explorecount = 0
    greedycount = 0
    totalgreedyhappiness = 0
    totalexploithappiness = 0
    totalexplorehappiness = 0
    while greedycount < t:
        thisSim = eGreedy(e)
        totalgreedyhappiness += thisSim
        greedycount += 1
    while explorecount < t:
        thisSim = exploreOnly()
        totalexplorehappiness += thisSim
        explorecount += 1
    while exploitcount < t:
        thisSim = exploitOnly()
        totalexploithappiness += thisSim
        exploitcount += 1
    greedyaverage = totalgreedyhappiness/greedycount
    exploreaverage = totalexplorehappiness / explorecount
    exploitaverage = totalexploithappiness / exploitcount
    exploreexpected = 100*h1 + 100*h2 +100*h3
    exploitexpected = h1 + h2 + h3 + 297*h3
    greedyexpected = 0.88*300*h3 + 0.04*300*h1 + 0.04*300*h2 + 0.04*300*h3
    print("optimum happiness -> 3300")
    print("greedy average happiness -> " + str(greedyaverage))
    print("explore average happiness -> " + str(exploreaverage))
    print("exploit average happiness -> " + str(exploitaverage))
    print("greedy average regret -> " + str(3300 - greedyaverage))
    print("explore average regret -> " + str(3300 - exploreaverage))
    print("exploit average regret -> " + str(3300 - exploitaverage))
    print("greedy expected happiness -> " + str(int(greedyexpected)))
    print("explore expected happiness -> " + str(exploreexpected))
    print("exploit expected happiness -> " + str(exploitexpected))
    print("greedy expected regret -> " + str(int(3300 - greedyexpected)))
    print("explore expected regret-> " + str(3300 - exploreexpected))
    print("exploit expected regret-> " + str(3300 - exploitexpected))
