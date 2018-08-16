a = int(input('Enter number A: '))
b = int(input('Enter number B: '))
c = int(input('Enter number C: '))

if a == b or a == c or b == c:
    a += 5
    b += 5
    c += 5
    print(a,b,c)
else:
    print('равных нет')


