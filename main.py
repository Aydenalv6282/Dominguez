import random
loops = 10000

''' 11% AND 9%
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

''' DICE
cnt = 0
for i in range(loops):
    remaining = [2,3,4,5,6,7,8,9,10,11,12]
    while len(remaining) > 0:
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        try:
            remaining.remove(dice1+dice2)
        except:
            pass
        cnt+=1

print(cnt/loops)
'''

