import time
import math

start = time.time()

# START

with open('p081_matrix.txt', 'r') as f:
# with open('test_matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split(',')] for line in f]

rows, cols = (len(matrix), len(matrix[0]))
distanceMatrix = [[0 for i in range(cols)] for j in range(rows)]

def updateCell(matrix, distanceMatrix, iteration, row, col):
    isChanged = False
    if (row - 1) >= 0:
        if distanceMatrix[row][col] + matrix[row-1][col] < distanceMatrix[row-1][col]:
            distanceMatrix[row-1][col] = distanceMatrix[row][col] + matrix[row-1][col]
            updateCell(matrix,distanceMatrix,iteration,row-1,col)
            isChanged = True
    if (col - 1) >= 0:
        if distanceMatrix[row][col] + matrix[row][col-1] < distanceMatrix[row][col-1]:
            distanceMatrix[row][col-1] = distanceMatrix[row][col] + matrix[row][col-1]
            updateCell(matrix,distanceMatrix,iteration,row,col-1)
            isChanged = True
    if (row + 1) <= iteration:
        if distanceMatrix[row][col] + matrix[row+1][col] < distanceMatrix[row+1][col]:
            distanceMatrix[row+1][col] = distanceMatrix[row][col] + matrix[row+1][col]
            updateCell(matrix,distanceMatrix,iteration,row+1,col)
            isChanged = True
    if (col + 1) <= iteration:
        if distanceMatrix[row][col] + matrix[row][col+1] < distanceMatrix[row][col+1]:
            distanceMatrix[row][col+1] = distanceMatrix[row][col] + matrix[row][col+1]
            updateCell(matrix,distanceMatrix,iteration,row,col+1)
            isChanged = True
    return isChanged

distanceMatrix[0][0] = matrix[0][0]

for iteration in range(1,cols):
    print(iteration)
    for row in range(0,iteration):
        distanceMatrix[row][iteration] = distanceMatrix[row][iteration-1] + matrix[row][iteration]
    for col in range(0,iteration):
        distanceMatrix[iteration][col] = distanceMatrix[iteration-1][col] + matrix[iteration][col]
    distanceMatrix[iteration][iteration] = min(distanceMatrix[iteration-1][iteration] + matrix[iteration][iteration], distanceMatrix[iteration][iteration-1] + matrix[iteration][iteration])
    exitFlag = False
    while not exitFlag:
        exitFlag = True
        isChanged = False
        for row in range(0,iteration):
            isChanged = updateCell(matrix, distanceMatrix, iteration, row, iteration)
            if isChanged:
                exitFlag = False
        for col in range(0,iteration):
            isChanged = updateCell(matrix, distanceMatrix, iteration, iteration, col)
            if isChanged:
                exitFlag = False
        isChanged = updateCell(matrix, distanceMatrix, iteration, iteration, iteration)
        if isChanged:
            exitFlag = False


# for col in range(1,cols):
#     for row in range(0,rows):
#         distanceMatrix[row][col] = distanceMatrix[row][col-1] + matrix[row][col]
#     exitFlag = False
#     while not exitFlag:
#         exitFlag = True
#         for row in range(0,rows):
#             if row != 0:
#                 if (distanceMatrix[row-1][col] + matrix[row][col]) < distanceMatrix[row][col]:
#                     distanceMatrix[row][col] = distanceMatrix[row-1][col] + matrix[row][col]
#                     exitFlag = False
#             if row != rows - 1:
#                 if (distanceMaatrix[row][col] = distanceMatrix[row+1][col] + matrix[row][col]
#                     exitFlag = False

for row in range(0, rows):
    print(distanceMatrix[row])
# print(distanceMatrix[rows-1][cols-1])

# END

end = time.time()
print(f'time: {end - start}')