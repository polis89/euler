import time
import math

start = time.time()

# START

cur_line = 0
cur_max = 0
cur_max_line = 0

with open('p099_base_exp.txt', 'r') as f:
    for line in f:
        cur_line += 1
        [base, power] = line.split(',')
        res = math.log(int(base), 10) * int(power)
        if res > cur_max:
            print(f'new max: {res} on line: {cur_line}')
            cur_max = res
            cur_max_line = cur_line

print(f'result: {cur_max_line}')



# END

end = time.time()
print(f'time: {end - start}')