# --- PSEUDOCODE PLAN ---
# 1. Define variables for a patient's age, weight, gender, and Cr concentration.
# 2. Check if age is less than 100. If false, report age needs correction.
# 3. Check if weight is greater than 20 and less than 80. If false, report weight needs correction.
# 4. Check if Cr is greater than 0 and less than 100. If false, report Cr needs correction.
# 5. Check if gender is 'male' or 'female'. If false, report gender needs correction.
# 6. If all variables are valid, calculate CrCl using the formula: ((140 - age) * weight) / (72 * Cr).
# 7. If the gender is female, multiply the final CrCl result by 0.85.
# 8. Print the calculated CrCl.

# --- ACTUAL CODE ---
age = 28          # in years
weight = 55       # in kg
gender = "female" # "male" or "female"
Cr = 50           # in µmol/l

# Validate inputs
if age >= 100:
    print("Error: Age needs to be corrected.")
elif weight <= 20 or weight >= 80:
    print("Error: Weight needs to be corrected.")
elif Cr <= 0 or Cr >= 100:
    print("Error: Cr needs to be corrected.")
elif gender not in ["male", "female"]:
    print("Error: Gender needs to be corrected.")
else:
    # Calculate CrCl
    crcl = ((140 - age) * weight) / (72 * Cr)
    
    # Apply female adjustment if necessary
    if gender == "female":
        crcl = crcl * 0.85
        
    print("The calculated CrCl is: " + str(crcl))