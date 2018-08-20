#Елка
for i in range(10):
    print('  ' * (10-i-1) + '* ' * (i*2+1))
print()

#Квадрат
for i in range(10):
    print('* ' * 10)
print()

##треугольник
for i in range(10):
    print('* '*i)
print()

#ромб
n = 11

print(((n - 1) * " " + "*"))

for i in range(2, n + 1):
    print(((n - i) * " " + "*" + ((i - 2) * 2 + 1) * "*" + "*"))

for j in range(n - 1, 1, -1):
    print(((n - j) * " " + "*" + ((j - 2) * 2 + 1) * "*" + "*"))

print(((n - 1) * " " + "*"))