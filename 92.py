import math

def produceNext(num):
    result = 0
    digitArray = [int(x) for x in str(num)]
    for x in digitArray:
        result += math.pow(x, 2)
    return int(result)

total = 10000000
countTo1 = 1
countTo89 = 0
leadTo1 = { 1 }
leadTo89 = { 89 }

for i in range(2, total):
    if total % i == 0:
        print(f'Progress: {100*i/total}%')
    val = i
    out = str(i)
    while True:
        newval = produceNext(val)
        out += ' -> ' + str(newval)
        if newval in leadTo89:
            countTo89+=1
            leadTo89.add(val)
            # print(out)
            # print(f'89: {summ}')
            break
        if newval in leadTo1:
            countTo1+=1
            leadTo1.add(val)
            # print(out)
            # print(f'1: {summ}')
            # print(summ)
            break
        val = newval
    # print('\n')
    
print(countTo89/total)
print(countTo89)
