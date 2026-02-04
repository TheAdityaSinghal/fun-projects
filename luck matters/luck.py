import numpy as np
import random

n = 0
epochs = 10
count = 1500000
candidates=150
for epoch in range(epochs):
    skill = {}
    luck = {}
    total = {}
    for i in range(count):
        skill[i]=random.randint(1,990)
        luck[i]=random.randint(1,10)
        total[i]=skill[i]+luck[i]
    skill_masters = sorted(total.items(), key=lambda x: x[1], reverse=True)[:candidates]
    life_masters = sorted(skill.items(), key=lambda x: x[1], reverse=True)[:candidates]
    ids_total = {x[0] for x in skill_masters}
    ids_skill = {x[0] for x in life_masters}
    n += len(ids_total & ids_skill)
    print(round((n / ((epoch+1) * candidates)) * 100,2))
n = (n / (epochs * candidates)) * 100
print(round((100-n)*candidates,2))
    