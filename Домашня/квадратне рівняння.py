print('Квадратне рівняння має вигляд: ax^2 + bx +1 c = 0')
a = float(input('Введіть значення а:'))
b = float(input('Введіть значення b:'))
c = float(input('Введіть значення с:'))

D = (b**2)-4*a*c

print(D)

if D > 0:
    x1 = (-b - (D ** 0.5)) / 2*a
    x2 = (-b + (D ** 0.5)) / 2*a

    print('x1=', x1, 'х2=', x2)

elif D == 0:
    x = -(b / 2*a)

    print(x)

else:
    print("розв'язку немає")
