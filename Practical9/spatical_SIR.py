# Define model parameters
# SET infection_rate = 0.3
# SET recovery_rate = 0.05

# Initialize 100x100 grid: 0 = Susceptible, 1 = Infected, -1 = Recovered
# CREATE grid WITH 100 rows AND 100 columns, FILLED WITH 0
# RANDOMLY SELECT ONE cell IN grid AND SET TO 1 (initial outbreak)

# Set up visualization
# START interactive plot

# Simulate 100 time steps
# FOR each time_step FROM 1 TO 100:
#     // Phase 1: Spread infection
#     FOR each infected_cell IN grid:
#         FOR each neighbor OF infected_cell:
#             IF neighbor IS susceptible AND random_chance ≤ infection_rate:
#                 SET neighbor TO infected
    
# Phase 2: Recovery
#     FOR each infected_cell IN grid:
#         IF random_chance ≤ recovery_rate:
#             SET infected_cell TO recovered
    
# Phase 3: Update visualization
#     DRAW grid WITH current states
#     SHOW current time_step
#     PAUSE briefly

# Finalize plot
# STOP interactive mode
# SHOW final plot





import numpy as np
import matplotlib.pyplot as plt
from random import random

BETA = 0.3
GAMMA = 0.05

population = np.zeros((100,100))
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1

plt.figure(figsize=(6, 4), dpi=150)
plt.ion()

time_point = 0
while time_point < 100:
    time_point += 1
    infected_locations = np.argwhere(population>0)
    
    for infected_location in infected_locations:
        neighbours = ((-1,-1),(-1,0),(-1,1),
                      (0,1),(0,-1),(1,1),(1,0),(1,-1))
        for neighbour in neighbours:
            x = infected_location[0] + neighbour[0]
            y = infected_location[1] + neighbour[1]
            if 0 <= x <= 99 and 0 <= y <= 99:
                if random() <= BETA and population[x,y] == 0:
                    population[x,y] = 1
    infected_locations = np.argwhere(population>0)
    for infected_location in infected_locations:
        x, y = infected_location[0], infected_location[1]
        if random() <= GAMMA:
            population[x,y] = -1
    
    plt.cla()  
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f'Time Step: {time_point}')
    plt.pause(0.1) 

plt.ioff()
plt.show()