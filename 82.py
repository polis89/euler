import time
import math

start = time.time()

# START

with open('p081_matrix.txt', 'r') as f:
# with open('test_matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

rows, cols = (len(matrix), len(matrix[0]))
distanceMatrix = [[0 for i in range(cols)] for j in range(rows)]

for row in range(0,rows):
    distanceMatrix[row][0] = matrix[row][0]

for col in range(1,cols):
    for row in range(0,rows):
        distanceMatrix[row][col] = distanceMatrix[row][col-1] + matrix[row][col]
    exitFlag = False
    while not exitFlag:
        exitFlag = True
        for row in range(0,rows):
            if row != 0:
                if (distanceMatrix[row-1][col] + matrix[row][col]) < distanceMatrix[row][col]:
                    distanceMatrix[row][col] = distanceMatrix[row-1][col] + matrix[row][col]
                    exitFlag = False
            if row != rows - 1:
                if (distanceMatrix[row+1][col] + matrix[row][col]) < distanceMatrix[row][col]:
                    distanceMatrix[row][col] = distanceMatrix[row+1][col] + matrix[row][col]
                    exitFlag = False

minimum = 0
for row in range(0, rows):
    if minimum == 0:
        minimum = distanceMatrix[row][cols-1]
    else:
        minimum = min(minimum, distanceMatrix[row][cols-1])

for row in range(0, rows):
    print(distanceMatrix[row])
print(minimum)

# END

end = time.time()
print(f'time: {end - start}')