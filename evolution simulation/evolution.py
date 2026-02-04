import numpy as np
import random
import math

count = [1]
reproduce = [10]
death = [9]
mutate = [1.5]
attack = [1]
defence = [1]

steps = 10000
wipe = 0
died = 0

def dead(specie):
    del count[specie]
    del reproduce[specie]
    del death[specie]
    del mutate[specie]


for step in range(steps):
    if not count:
        wipe+=1
        count = [1]
        reproduce = [10]
        death = [10]
        mutate = [1]
    specie = 0
    while specie < len(count):
        if count[specie]==0:
            died+=1
            dead(specie)
            continue
        #reproduce
        r = random.uniform(1,100)
        resource_factor = max(0.0, 1 - sum(count)/100000)
        if r <= reproduce[specie]*resource_factor:
            count[specie] = math.ceil(count[specie] * 1.1 * resource_factor)
        #death
        d = random.uniform(1,100)
        resource_factor = max(0.0, 1 - sum(count)/100000)
        if d <= death[specie]:
            if count[specie]==1 or resource_factor==0.0:
                died+=1
                dead(specie)
                continue
            count[specie] = count[specie]//(1.1 * resource_factor)
        # attack
        '''a = random.uniform(1,100)
        if a <= attack[specie]:
            war = random.randint(1,len(count))
            if war!=specie:
                dead(war)
                died+=1
                continue'''
        #mutate
        m = random.uniform(1,100)
        if m <= mutate[specie]:
            count.append(1)
            #reproduce
            r = random.randint(1,10)
            sign = random.choice([-1,1])
            reproduce.append(reproduce[specie]*(1+sign*(r/100)))
            #death
            d = random.randint(1,10)
            sign = random.choice([-1,1])
            death.append(death[specie]*(1+sign*(d/100)))
            #mutate
            m = random.randint(1,10)
            sign = random.choice([-1,1])
            mutate.append(mutate[specie]*(1+sign*(m/100)))
        specie+=1
    if step%1000==0:
        print(count)
'''
print("\ndone!\n")
print(count)
print(list(round(r,1) for r in reproduce))
print(list(round(r,1) for r in death))
print(list(round(r,1) for r in mutate))'''

print("\nstats\n")

#general 
print(count)
print("species dead = ", died)
print("life wiped out = ", wipe)
#reproduce
print("Highest reproduction rate: ", max(reproduce))
avg_repro = sum(reproduce[i] for i,c in enumerate(count))/len(count)
print("avg reproduce rate for alive species: ", avg_repro)
#death
print("Lowest death rate: ", min(death))
avg_death = sum(death[i] for i,c in enumerate(count))/len(count)
print("avg death rate for alive species: ", avg_death)
#mutate
print("Lowest mutatation rate: ", min(mutate))
avg_mutate = sum(mutate[i] for i,c in enumerate(count))/len(count)
print("avg mutate rate for alive species: ", avg_mutate)