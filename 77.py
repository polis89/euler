import time
from utils import isPrime

start = time.time()

# START

primes = []

for x in range(2, 100000):
    if isPrime(x):
        primes.append(x)

accTable = {
    0: 1,
    2: 1
}

current = 3

while current < 11:
    print('---')
    count = 0
    for x in primes:
        if x > current:
            break
        if (current - x) in accTable:
            count += accTable[current-x]
            if (current - x) != x and (current - x) in primes and accTable[current-x] > 0:
                count -= 0.5
            print(f'-- {x} plus {accTable[current-x]} variants from {current-x}')
    print(f'Number: {current}. Variants: {count}')
    accTable[current] = count
    current += 1


# print(primes)



# END

end = time.time()
print(f'time: {end - start}')