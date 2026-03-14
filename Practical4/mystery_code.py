# What does this piece of code do?
# Answer: It calculates and prints the total sum of 11 
# randomly generated integers (each between 1 and 10).

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

total_rand = 0 # Initialization
progress=0 # Initialization
while progress<=10: # Loops 11 times
	progress+=1
	n = randint(1,10) # Draws a random integer between 1 and 10 and assigns it to 'n'.
	total_rand+=n # Adds it to the running total.

print(total_rand)

