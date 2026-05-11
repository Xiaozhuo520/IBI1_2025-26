import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dalys_data = pd.read_csv("/Users/wangxiaozhuo/IBI/IBI1_2025-26/Practical10/dalys-rate-from-all-causes.csv")


# First 10 rows and maximum DALYs
first_10_data = dalys_data.iloc[0:10, 2:4]
print("--- First 10 Rows (Year & DALYs) ---")
print(first_10_data)

afghanistan_first_10 = dalys_data.head(10)
max_year_afg = afghanistan_first_10.loc[afghanistan_first_10['DALYs'].idxmax(), 'Year']
print(f"Max DALYs year in first 10 rows: {max_year_afg}")
# The year that reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan is 1990.

# Zimbabwe Boolean
zimbabwe_mask = dalys_data['Entity'] == 'Zimbabwe'
zimbabwe_years = dalys_data.loc[zimbabwe_mask, 'Year']
print("\n--- Zimbabwe Years ---")
print(zimbabwe_years)
# The first year for which data were recorded in Zimbabwe is 1990 and the last year is 2019.


# 2019 Min and Max DALYs
recent_data = dalys_data.loc[dalys_data['Year'] == 2019, ["Entity", "DALYs"]]

max_country = recent_data.loc[recent_data['DALYs'].idxmax(), 'Entity']
min_country = recent_data.loc[recent_data['DALYs'].idxmin(), 'Entity']
print("\n--- 2019 Min/Max Countries ---")
print(f"Country with Maximum DALYs: {max_country}")
print(f"Country with Minimum DALYs: {min_country}")
# The country with the maximum DALYs in 2019 is the Central African Republic, and the country with the minimum is San Marino.

# Plotting DALYs over time
target_country_data = dalys_data.loc[dalys_data['Entity'] == max_country]

plt.figure(figsize=(10, 6))
plt.plot(target_country_data['Year'], target_country_data['DALYs'], 'r-o')
plt.title(f'DALYs Over Time for {max_country}')
plt.xlabel('Year')
plt.ylabel('DALYs (Disability-Adjusted Life Years)')
plt.xticks(target_country_data['Year'], rotation=-90)
plt.grid(True)
plt.tight_layout()
plt.show()

# Task 5: Asking one other question
plt.figure(figsize=(10, 6))
plt.hist(recent_data['DALYs'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title('Distribution of DALYs Across All Countries in 2019')
plt.xlabel('DALYs')
plt.ylabel('Number of Countries')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.show()