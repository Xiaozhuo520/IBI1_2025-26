import numpy as np
import matplotlib.pyplot as plt

N = 10000
BETA = 0.3
GAMMA = 0.05


time_points = [(N-1,1,0),]
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

time = list(range(len(time_points)))

susceptibles = [i[0] for i in time_points]
infecteds = [i[1] for i in time_points]
resistants = [i[2] for i in time_points]


plt.plot(time, susceptibles, label='susceptible')
plt.plot(time, infecteds, label='infecteds')
plt.plot(time, resistants, label='resistant')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.savefig('SIR_plot_vaccination.png')
plt.show()


    