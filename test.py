sleep_hours = (5,6,7,6,6,7,6,5,6,7,7,8,6,5,4,6,7,5,8,7)
weekly_averange = []
for i in range(len(sleep_hours) - 7):
    weekly_sum = sum(sleep_hours[i:i+7])
    weekly_averange.append(round(weekly_sum/7, 2))
print(weekly_averange)


