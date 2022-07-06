import time
import math

start = time.time()

# START

with open('p081_matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

rows, cols = (80, 80)
distanceMatrix = [[0 for i in range(cols)] for j in range(rows)]

for iteration in range(0,rows):
    if iteration == 0:
        distanceMatrix[iteration][iteration] = matrix[iteration][iteration]
    else:
        for row in range(0, iteration):
            if row == 0:
                distanceMatrix[row][iteration] = distanceMatrix[row][iteration-1] + matrix[row][iteration]
            else:
                distanceMatrix[row][iteration] = min(
                    distanceMatrix[row-1][iteration] + matrix[row][iteration],
                    distanceMatrix[row][iteration-1] + matrix[row][iteration]
                )
        for column in range(0, iteration):
            if column == 0:
                distanceMatrix[iteration][column] = distanceMatrix[iteration-1][column] + matrix[iteration][column]
            else:
                distanceMatrix[iteration][column] = min(
                    distanceMatrix[iteration-1][column] + matrix[iteration][column],
                    distanceMatrix[iteration][column-1] + matrix[iteration][column]
                )
        distanceMatrix[iteration][iteration] = min(
            distanceMatrix[iteration-1][iteration] + matrix[iteration][iteration],
            distanceMatrix[iteration][iteration-1] + matrix[iteration][iteration]
        )

print(distanceMatrix)
# END

end = time.time()
print(f'time: {end - start}')