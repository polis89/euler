import time

start = time.time()

# START
count = 0
count_negative = 0

# cross product between AB and AC
def crossProduct(a,b,c):
    a_x = b[0] - a[0]
    a_y = b[1] - a[1]
    b_x = c[0] - a[0]
    b_y = c[1] - a[1]
    return a_x * b_y - b_x * a_y

with open('p102_triangles.txt', 'r') as f:
    for line in f:
        parsed = [int(num) for num in line.split(',')]
        x = parsed[0:2]
        y = parsed[2:4]
        z = parsed[4:6]
        if x[0] <0 and y[0] < 0 and z[0] <0:
            count_negative += 1
            continue
        if x[1] <0 and y[1] < 0 and z[1] <0:
            count_negative += 1
            continue
        if x[0] >0 and y[0] > 0 and z[0] >0:
            count_negative += 1
            continue
        if x[1] >0 and y[1] > 0 and z[1] >0:
            count_negative += 1
            continue
        
        cP1 = crossProduct(x,y,[0,0])
        cP2 = crossProduct(y,z,[0,0])
        cP3 = crossProduct(z,x,[0,0])

        if cP1 >= 0 and cP2 >= 0 and cP3 >= 0:
            count += 1
            continue
        if cP1 <= 0 and cP2 <= 0 and cP3 <= 0:
            count += 1
            continue
        count_negative += 1

# END

print(count)
print(count_negative)
end = time.time()
print(f'time: {end - start}')