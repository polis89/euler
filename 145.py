import time

start = time.time()

# START

sum = 2
count = 0

for i in range(2,100):
    for p in range(1,3):
        if i % pow(10,p) == 0:
            sum -= 18
    sum += 2
    flag = True
    for d in str(sum):
        if int(d) % 2 == 0:
            flag = False
            break
    if flag:
        count += 1
    print(f'checking: {i}. sum: {sum}')
# END

end = time.time()
print(f'time: {end - start}')