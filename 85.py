import time
import math

start = time.time()

# START

foundmin = 2000000

def rectCount(m,n):
    return (m * n * (n + 1) * (m + 1)) / 4 

for width in range(1,2000):
    for height in range(1,2000):
        count = rectCount(width,height)
        # print(f'Width: {width} Height: {height}. Count: {count}\n')
        if foundmin > abs(2000000-count):
            minwidth = width
            minheight = height
            foundmin = min(foundmin, abs(2000000-count))
            print(f'Width: {width} Height: {height}. Count: {count}\n')


# END
print(foundmin)
print(minwidth)
print(minheight)

end = time.time()
print(f'time: {end - start}')