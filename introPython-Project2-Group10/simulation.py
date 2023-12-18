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
    print("greedy average -> " + str(greedyaverage))
    print("explore average -> " + str(exploreaverage))
    print("exploit average -> " + str(exploitaverage))
    print("greedy average regret -> " + str(3300 - greedyaverage))
    print("explore average regret -> " + str(3300 - exploreaverage))
    print("exploit average regret -> " + str(3300 - exploitaverage))
    print("greedy expected -> " + str(greedyexpected))
    print("explore expected -> " + str(exploreexpected))
    print("exploit expected -> " + str(exploitexpected))
    print("greedy expected regret -> " + str(int(3300 - greedyexpected)))
    print("explore expected regret-> " + str(3300 - exploreexpected))
    print("exploit expected regret-> " + str(3300 - exploitexpected))
