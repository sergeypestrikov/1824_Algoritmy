# По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним

a = int(input('Введите длину стороны a: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

if a + b > c and a + c > b and b + c > a and min(a, min(b, c)) > 0:
    if a == b == c:
        print('Треугольник равносторонний')
    elif a == b or a == c or b==c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Такого треугольника быть не может')