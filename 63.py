import math

count = 0

for i in range(1,10):
    for power in range(1,100):
        result = math.pow(i,power)
        if len(str(int(result))) == power:
            print(f"Number: {int(result):n} is a power {power} of {i}")
            count+=1

print(f'result: {count}')
        