# --- PSEUDOCODE / PLAN ---
# 1. Define the total population size.
# 2. Define the initial number of infected students.
# 3. Define the daily growth rate.
# 4. Initialize a day counter starting at Day 1.
# 5. Loop while the number of infected students is less than 91:
# 6.     print the current day and the number of infected students.
# 7.     Update the number of infected students by adding the newly infected individuals (current * growth rate).
# 8.     Increase the day counter by 1 for the next iteration.
# 9. Print the final day's numbers.
# 10. Report the total number of days it took to infect the entire class.



# 1. Define the total population size
total_students = 91

# 2. Define the initial number of infected students
infected_students = 5

# 3. Define the daily growth rate
growth_rate = 0.4

# 4. Initialize a day counter
day = 1

# 5. Loop until everyone is infected
while infected_students < total_students:
    
    # 6. Display the number of infected students for the current day
    print(f"Day {day}: {infected_students:.2f} students infected")
    
    # 7. Calculate the new number of infected students for the next day
    infected_students = infected_students + (infected_students * growth_rate)
    
    # 8. Increase the day counter
    day = day + 1

# Cap the final number at 91 in case the math pushes it slightly over the total class size
if infected_students > total_students:
    infected_students = total_students

# 9. Print the final day (when the loop condition is finally met)
print(f"Day {day}: {infected_students} students infected")

# 10. Report how many days it took
print(f"It took {day} days for all {total_students} students in the IBI1 class to become infected.")