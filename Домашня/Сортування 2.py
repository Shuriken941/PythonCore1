a = list(input('Введіть символи:'))
word = []
num = []

for i in a:
    if i.isnumeric():
        num.append(int(i))
    else:
        word.append(i)

word.sort()
num.sort()
print(num + word)