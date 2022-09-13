import random
import numpy
import math
import time
from matplotlib import pyplot as plt

loops = 1000

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
'''# RANDOM WALK PROBLEM
totdist = 0
absdist = 0
loops = 100000
x_vals = []
y_vals = []
for s in range(loops):
    x_vals.append(s)
    dist = 0
    for d in range(100):
        dist += random.choice([-1, 1])
    adist = abs(dist)
    y_vals.append(dist)
    totdist += dist
    absdist += adist
print("Average distance, positive/negative:", totdist/loops)
print("Average absolute distance:", absdist/loops)
plt.scatter(x_vals, y_vals, color="blue", s=1)
plt.show()
'''
# Single Server Queuing model
T = 9  # Does this represent the maximum time that the server lets new customers in? Does this mean that customers
# cannot arrive after 9 units of time even though the mean time of arrival is 10 units? Won't customers not make it
# most of the time? This is assumed.
E = 20  # Server usage time calculation
P = 10  # Customer arrival time calculation
total_time = 0
total_service_time = 0
total_idle_time = 0
total_over_time = 0
total_customer_count = 0
PRINT_RAW_DATA = True
if PRINT_RAW_DATA:
    print("Parameters:\nT:", T, "\nExponential:", E, "\nPoisson:", P)
for l in range(loops):
    # Keep in mind that time = service_time + idle_time
    arrival_time = 0  # Variable only relevant for the beginning calculations, not printed
    service_time = 0
    idle_time = 0
    queue = 0
    customer_arrivals = [0]  # List of ARRIVAL times, not including usage.
    customer_use_times = []
    interval = 0
    while arrival_time <= T:  # Calculates when all customers initially arrive
        interval = numpy.random.poisson(P)
        arrival_time += interval  # Time DOES NOT include the usage time yet.
        if arrival_time <= T:
            customer_arrivals.append(arrival_time)
            if queue == 0:
                idle_time += interval
            queue += 1
        elif queue == 0:
            idle_time = T
    customer_arrivals.pop(0)
    for q in range(queue):  # Adds usage time to initial calculations
        usage = numpy.random.exponential(E)
        service_time += usage
        customer_use_times.append(service_time)
        if q != queue - 1:
            diff = customer_arrivals[q + 1] - (customer_arrivals[q] + usage)
            if diff > 0:  # Determines if usage time overlaps with idle time
                idle_time += diff
    time = service_time + idle_time
    over_time = time - T
    if PRINT_RAW_DATA:
        print("=====", "\nCustomer Arrival Times:", customer_arrivals, "\nCustomer Usage Times:", customer_use_times,
              "\nIdle Time:", idle_time, "\nService Time:", service_time, "\nTime:", time,
              "\nOvertime:", over_time, "\nQueue:", queue)
    total_time += time
    total_service_time += service_time
    total_idle_time += idle_time
    total_over_time += over_time
    total_customer_count += queue
if PRINT_RAW_DATA:
    print("==========\n"
          "Average data over", loops, "runs:", "\n\nTotal Customers:", total_customer_count, "\nAverage Customers:",
          total_customer_count/loops, "\nTotal Service Time:", total_service_time, "\nAverage Service Time:",
          total_service_time/loops, "\nTotal Idle Time:", total_idle_time, "\nAverage Idle Time:",
          total_idle_time/loops, "\nTotal Over Time:", total_over_time, "\nAverage Over Time:",
          total_over_time/loops, "\nTotal Server Time:", total_time, "\nAverage Server Time:", total_time/loops,
          "\n==========")
'''
Answer For #2:
If you wanted information for the amount of idle time the server experiences in a day, you'd need to specify a unit of
time first. If the unit of time is 1 minute, then you'd simply change the variable T from 9 to 1440. If T represents 1
hour, then T would be changed to 24.
'''
