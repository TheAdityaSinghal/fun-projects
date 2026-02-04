import random
import numpy as np

population = [1000,500,700]
countries = len(population)
healthy = population.copy()
infected = [0]*countries
dead = [0]*countries
recovered = [0]*countries

# ground 0
infected[0]+=1
healthy[0]-=1
infected[1]+=1
healthy[1]-=1
infected[2]+=1
healthy[2]-=1

days = 70
meet = 10
chances = 1
cure_found=False
cure_easiness=0.5

for day in range(days):
    #intra country transmission 
    for country in range(countries):
        increase_per_country=0
        for person in range(infected[country]):
            increase_per_person=0
            for meetup in range(meet):
                badluck = random.uniform(0,100)
                if badluck<=chances:
                    increase_per_person+=1
            increase_per_country+=increase_per_person
        infected[country] = min(population[country],infected[country] + increase_per_country)
        healthy[country] = population[country] - infected[country]
    #cure
    if not cure_found:
        cure_odds = random.uniform(0,100)
        if cure_odds < cure_easiness:
            cure_found=True
    # recovering
    for country in range(countries):
        



    #print(healthy, infected)