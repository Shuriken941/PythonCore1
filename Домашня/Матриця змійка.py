n = int(input('Кількість лінійок '))
m = int(input('Кількість ствовпців'))
for j in range(n):
    print('\t '.join([str(i + 1 + m * j) for i in range(m)][::pow(-1, j)]))
