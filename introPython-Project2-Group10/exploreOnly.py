import random


def exploreOnly():
    totalhappiness = 0
    c1 = 0
    c2 = 0
    c3 = 0
    while c1 < 100:
        totalhappiness += random.normalvariate(h1,d1)
        c1 += 1
    while c2 < 100:
        totalhappiness += random.normalvariate(h2,d2)
        c2 += 1
    while c3 < 100:
        totalhappiness += random.normalvariate(h3,d3)
        c3 += 1
    return totalhappiness
