import random
import numpy
import math
import time
from matplotlib import pyplot as plt

loops = 1000000

''' #11% AND 9%
result = None
avg = [0,0,0,0,0,0,0,0,0,0]
for i in range(loops):
    rand = random.random()
    if rand < .11:
        avg[0] += 1
        result = 5
    elif rand < .22:
        avg[1] += 1
        result = 7
    elif rand < .33:
        avg[2] += 1
        result = 9
    elif rand < .44:
        avg[3] += 1
        result = 11
    elif rand < .55:
        avg[4] += 1
        result = 13
    elif rand < .64:
        avg[5] += 1
        result = 6
    elif rand < .73:
        avg[6] += 1
        result = 8
    elif rand < .82:
        avg[7] += 1
        result = 10
    elif rand < .91:
        avg[8] += 1
        result = 12
    elif rand < 1.00:
        avg[9] += 1
        result = 14

avg = [x/loops for x in avg]
print(avg)
'''

'''# ROLLING 2 DICE
loops = 10000
rolls = 0
for i in range(loops):
    sums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while len(sums) != 0:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dsum = dice1 + dice2
        if sums.__contains__(dsum):
            sums.remove(dsum)
        rolls += 1

print(rolls / loops)
'''

'''#INVERSE TRANSFORM METHOD
x_vals = []
y_vals = []

# Original Equation
for x in range(100):
    x = x / 100
    y = (x ** 2 + x) / 2
    x_vals.append(x)
    y_vals.append(y)

plt.plot(x_vals, y_vals, color="red")  # Original

x_vals = []
y_vals = []

for x in range(100):
    x = x / 100
    y = (-1 + abs((1 + 8 * x) ** .5)) / 2
    x_vals.append(x)
    y_vals.append(y)

plt.plot(x_vals, y_vals, color="blue")  # Inversed


def distribution(num):  # Distribution: f(x)=(x^2+x)/2
    return (-1 + abs((1 + 8 * num) ** .5)) / 2


counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Counts from 0-9
for i in range(loops):
    num = random.random()
    ztn = int(distribution(num) * 10)
    print(num, ":", ztn)
    counts[ztn] += 1

print("How many times each number from 0-9 showed up:")
print(counts)

plt.show()
'''

'''#RANDOM NUMBER INTERVAL
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
nums = []
x_vals = []
for i in range(loops):
    ran = random.random()*(b-1)+a
    x_vals.append(i)
    nums.append(ran)
plt.scatter(x_vals, nums, color="red", s=1)
plt.show()
'''

'''
# RANDOM NUMBER DISTRIBUTION
gmean = int(input("Enter the desired mean: "))
gstan = int(input("Enter the desired standard deviation: "))

equal_dist = []
defined_dist = []
x_vals = []

for i in range(loops):
    ran = (random.random()-.5)*3.5  # Shifts the number to have a mean of 0 and std of 1
    ran_ctrl = ran*gstan+gmean
    equal_dist.append(ran)
    defined_dist.append(ran_ctrl)
    x_vals.append(ir)

plt.scatter(x_vals, equal_dist, color="blue", s=1)
plt.scatter(x_vals, defined_dist, color="red", s=1)

print("Estimated Mean: ", numpy.mean(defined_dist))
print("Estimated Standard Deviation: ", numpy.std(defined_dist))
plt.show()
'''

'''# POISSSON BUS
rate = 5
x_values = []
num_people = []
for x in range(loops):
    x_values.append(x)
    gen = numpy.random.poisson(rate)  # Given a mean, it uses poisson distribution to generate a random number.
    people = 0
    for b in range(gen):
        carry = random.randint(20, 40)
        people += carry
    num_people.append(people)
plt.plot(x_values, num_people, color="red")

sum_people = [num_people[0]]
for b in range(1, len(num_people)):
    sum_people.append(sum_people[b-1]+num_people[b])

plt.plot(x_values, sum_people, color="blue")
plt.show()
'''
'''# Casualty Insurance
rate = 800
greater_count = 0
cnt = 0
for i in range(loops):
    sum = 0
    for x in range(1000):
        ran = random.random()
        if ran < 0.05:
            sum += numpy.random.exponential(rate)
    if sum > 50000:
        greater_count += 1
print(str((greater_count/loops)*100)+"%")
'''
'''# Sphere Problem
ins = 0
for n in range(loops):
    xran = (random.random()-.5)*2
    yran = (random.random()-.5)*2
    zran = (random.random()-.5)*2
    dist = math.sqrt(xran**2+yran**2+zran**2)
    if dist <= 1:
        ins += 1
per = ins/loops
print(per*8)
'''
