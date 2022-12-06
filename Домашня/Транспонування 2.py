import numpy as np

x = int(input('Введіть значення x:'))
y = int(input('Введіть значення y:'))

matrix = [[0]*y for i in range(x)]
a = 1
for i in range(x):
    for j in range(y):
        matrix[i][j] = a
        a += 1

def printingMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t ')
        print()
    return

def transpouse(matrix):
    matrix_transpouse = np.array(matrix).transpose()
    return matrix_transpouse

print(Print_matrix(matrix))
print(Print_matrix(transpouse(matrix)))