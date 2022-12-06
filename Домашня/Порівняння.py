a = list(input('Введіть символи:'))
b = list(input('Введіть символи:'))
if len(a) == len(b):
    for i, c in zip(a, b):
        if i == c:
            print('True=', i, c)
        else:
            print('False=', i, c)
else:
    print("довжина не співпадає")
