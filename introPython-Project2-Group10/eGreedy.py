import random

#when entering e value make sure it is entered as a decimal and not the percent value
h1 = 9
h2 = 7
h3 = 11
d1 = 3
d2 = 5
d3 = 7

def eGreedy(e):
#defining the variables that will be used later
#the "happiness" variables correspond to your current total happiness at a single cafeteria
#the "count" variables correspond to the amount of times you have been to a cafeteria
#the "avg" variables correspond to your average happiness for each time you have been to a cafeteria
    caf1happiness = 0
    caf2happiness = 0
    caf3happiness = 0
    caf1avg = 0
    caf2avg = 0
    caf3avg = 0
    caf1count = 0
    caf2count = 0
    caf3count = 0
    totalhappiness = 0
    mealcount = 0
#creates a while loop that runs 300 times
    while mealcount < 300:
#calculates the current average happiness each time through the loop, the if statements help to avoid a % by 0 error if you have not been to a certain cafeteria yet
        if caf1count > 0:
            caf1avg = caf1happiness/caf1count
        if caf2count > 0:
            caf2avg = caf2happiness/caf2count
        if caf3count > 0:
            caf3avg = caf3happiness/caf3count
#if you havent gone to a cafeteria yet or if the random number you generate is in the e percent of times you go to a cafeteria
        if random.random() > (1-e) or mealcount < 1:
#chooses a random number between 1 to 3 and you go to that cafeteria
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
 #if the random number generated isnt in the e percentage of times than you go to the cafeteria then you go to the cafeteria with the current highest average happiness
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
    print(totalhappiness)

