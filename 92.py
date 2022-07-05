import math
import time

squaresLookup = {
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16,
    5: 25,
    6: 36,
    7: 49,
    8: 64,
    9: 81
}

def produceNext(num):
    result = 0
    digitArray = [int(x) for x in str(num)]
    for x in digitArray:
        result += squaresLookup[x]
    return int(result)

start = time.time()

countTo1 = 1
countTo89 = 0
leadTo1 = { 1 }
leadTo89 = { 89 }

for i in range(2, 10000000):
    val = i
    out = str(i)
    while True:
        newval = produceNext(val)
        # out += ' -> ' + str(newval)
        if newval in leadTo89:
            countTo89+=1
            if val < 700: leadTo89.add(val)
            break
        if newval in leadTo1:
            if val < 700: leadTo1.add(val)
            break
        val = newval
    # print('\n')
    
print(countTo89)

end = time.time()
print(f'time: {end - start}')

# best time: 23.756940364837646