import matplotlib.pyplot as plt


HRs = (72,60,126,85,90,59,76,131,88,121,64)
print(f'{len(HRs)} patients in total, and average heart rate is {sum(HRs)/len(HRs)}')
low, normal, high = [],[],[]
for HR in HRs:
    if HR < 60:
        low.append(HR)
    elif HR > 120:
        high.append(HR)
    else:
        normal.append(HR) 
print(f'low: {len(low)}, normal: {len(normal)}, high: {len(high)}')       
if len(low) > len(normal):
    if len(low) > len(high):
        print('Most people have low heart rate')
else:
    if len(normal) > len(high):
        print('Most people have normal heart rate')
    else:
        print('Most people have high heart rate')

labels = ('low', 'normal', 'high')
numbers = (len(low), len(normal), len(high))

plt.pie(numbers, labels=labels, autopct='%1.1f%%')
plt.title("Distribution of Heart Rate Categories")
plt.show()