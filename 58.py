from utils import isPrime

numbersInDiagonal = 1
primeNumnbersInDiagonal = 0
lastnumber = 1

for level in range(2,100000):
    numbersInDiagonal+=4
    for i in range(0,4):
        lastnumber += 2 * (level - 1)
        if isPrime(lastnumber):
            primeNumnbersInDiagonal += 1
    print(f'Level {level}: primes - {primeNumnbersInDiagonal}, total - {numbersInDiagonal}, result - {primeNumnbersInDiagonal / numbersInDiagonal}')
    if primeNumnbersInDiagonal / numbersInDiagonal < 0.1:
        print(f'FOUND: {2 * (level - 1) + 1}')
        break