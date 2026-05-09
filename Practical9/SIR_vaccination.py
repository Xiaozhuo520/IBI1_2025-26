import numpy as np
import matplotlib.pyplot as plt

N = 10000
BETA = 0.3
GAMMA = 0.05

def infection_with_vaccination(rate):
    if N-1-int(N*rate) >= 0:
        time_points = [(N-1-int(N*rate),1,int(N*rate)),]
    else:
        time_points = [(0,0,N),]
    while len(time_points) < 1000:
        
        now = time_points[-1]
        susceptible,infected,resistant = now
        p_infected = BETA * infected / N
        p_recovery = GAMMA
        
        now_infected = sum(np.random.choice(
            range(2),susceptible,p=[1-p_infected,p_infected])) 
        susceptible -= now_infected
        infected += now_infected

        now_recovered = sum(np.random.choice(
            range(2),infected,p=[1-p_recovery,p_recovery])) 
        infected -= now_recovered
        resistant += now_recovered

        time_points.append((susceptible,infected,resistant))

    infecteds = [i[1] for i in time_points]
    return infecteds
    
time = list(range(1000))

for i in range(11):
    plt.plot(time,infection_with_vaccination(i/10),label=f'{i*10}%')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.savefig('SIR_plot.png')
plt.show()


    