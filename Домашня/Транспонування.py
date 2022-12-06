
x = int(input('Введіть значення x:'))
y = int(input('Введіть значення y:'))

matrix = [[0]*y for i in range(x)]
a = 1

for i in range(x):
    for j in range(y):
        matrix[i][j] = a
        a += 1


def Print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end='\t ')
        print()
    return

def transpouse(matrix):
    matrix_transpouse = []
    for i in range(len(matrix[0])):
        matrix_transpouse.append(list())
        for j in range(len(matrix)):
            matrix_transpouse[i].append(matrix[j][i])
    return matrix_transpouse

Print_matrix(matrix)
print(Print_matrix(transpouse(matrix)))