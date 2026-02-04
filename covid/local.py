import random 
import matplotlib.pyplot as plt

s = 1000
i = 1
c = 0
d = 0
g = s + c
r = c + d
n = s + i + c

beta = 0.1 # infections odd
gamma = 0.01 # deaths odd
alpha = 0.02 # cure odd
days = 700

S = [s]
I = [i]
C = [c]
C_new = [c]
D = [d]
R = [r]
G = [g]

reinfection = 49


for day in range(days):

    s_prev = s
    i_prev = i
    c_prev = c
    d_prev = d

    infections_odd = beta * random.uniform(0.8,1.2)
    death_odd = gamma * random.uniform(0.8,1.2)
    cure_odd = alpha * random.uniform(0.8,1.2)

    new_removed = (death_odd+cure_odd) * i_prev
    new_infections = infections_odd * ((s_prev * i_prev) / n)
    if day>=49:
        c_add = i_prev*(cure_odd) - C_new[day-reinfection]
    else:
        c_add = i_prev*(cure_odd)
    c = c_prev + c_add
    d = d_prev + i_prev*(death_odd)
    if day>=49:
        s = s_prev - new_infections + C_new[day-reinfection]
    else:
        s = s_prev - new_infections
    i = i_prev + new_infections - new_removed

    r = c + d
    g = c + s
    n = s + i + c + d

    S.append(s)
    I.append(i)
    R.append(r)
    C.append(c)
    C_new.append(c_add)
    D.append(d)
    G.append(g)

    if day%10==0:
        alpha *= 1
        beta *=1.03
        gamma *=1.01
    if day%20==0:
        print(f"day: {day+1} --> n: {int(n)}, s: {int(s)}, i: {int(i)}, c: {int(c)}, d: {int(d)}, r: {int(r)}, n: {int(g)}")
    '''if day%100==0:
        alpha *= 2
        reinfection += 40'''
    '''if day % 100 == 0:
        beta *= 2
        gamma *= 1.2'''
    if int(i) == 0: #or int(s) <= 0:
        break

plt.plot(S, label = "Healthy")
plt.plot(I, label = "Infected")
plt.plot(R, label = "Removed")
plt.plot(C, label = "Cured")
plt.plot(D, label = "Dead")
plt.plot(G, label = "Normal")
plt.xlabel("Days")
plt.ylabel("People")
plt.legend()
plt.show()
