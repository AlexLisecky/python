#По введенным пользователем длинам трех отрезков определить, можно ли составить из этих отрезков треугольник.
# Если да, определить, будет ли треугольник разносторонним, равнобедренным или равносторонним.

a = int(input('Введите длину треугольника: '))
b = int(input('Введите длину треугольника: '))
c = int(input('Введите длину треугольника: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Невозможный треугольник')
elif a != b and b!= c and c!= a:
    print('Треугольник разносторонний')
elif a == b == c:
    print('Треугольник равносторонний')
else:
    print('Треугольник равнобедренный')