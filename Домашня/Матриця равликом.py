n = int(input())  # размер матрицы
a = [[0] * n for i in range(n)]
count = 0  # количество заполненных ячеек
for i in range(n):   # заполнение 1 строки
    count += 1
    a[0][i] = count
j = 0
i = n-1
n -= 1
while len(a)**2 != count:  #умова виходу з циклу
    for k in range(n):  #рух вниз
        j += 1
        count += 1
        a[j][i] = count  # заповнення матриці
    for k in range(n):  #рух в ліво
        i -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1):  #рух в верх
        j -= 1
        count += 1
        a[j][i] = count
    for k in range(n-1): #рух в право
        i += 1
        count += 1
        a[j][i] = count
    n -= 2    #перехід на нижчий рівень
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end='\t')
    print()