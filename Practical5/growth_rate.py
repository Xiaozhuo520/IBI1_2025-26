import matplotlib.pyplot as plt

population_data = {
    'UK': (66.7, 69.2),
    'China': (1426, 1410),
    'Italy': (59.4, 58.9),
    'Brazil': (208.6, 212.0),
    'USA': (331.6, 340.1)
}
percent_changes = {}
for country in population_data:
    percent_changes[country] = \
    (population_data[country][1] - population_data[country][0]) / population_data[country][0] * 100
for country in percent_changes:
    print(f'The percent change of {country} is {percent_changes[country]:.4f}')

sorted_countries = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)
for country in sorted_countries:
    print(country[0], end=', ')

print(f"Country with the largest increase is {sorted_countries[0][0]}, and the largest decrease is {sorted_countries[-1][0]}.")

plt.bar(percent_changes.keys(),percent_changes.values())
plt.title("Population Percentage Change (2020-2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.show()
