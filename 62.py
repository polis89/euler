import math
import time
from utils import isPermutation

start = time.time()

cubes = set()

for x in range(5, 10000):
    cubes.add(int(math.pow(x, 3)))

for a in cubes:
    cubesCount = 1
    perms = [a]
    for b in cubes:
        if b != a and isPermutation(a,b):
            cubesCount += 1
            perms.append(b)
        if cubesCount > 5:
            break
    if cubesCount == 5:
        print(f'FOUND: {a}')
        print(perms)
        break

end = time.time()
print(f'time: {end - start}')
# print(cubes)
# print(isPermutation(12234516789,98713321654))