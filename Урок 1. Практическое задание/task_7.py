"""
7. По длинам трех отрезков, введенных пользователем,
определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует,
то определить, является ли он разносторонним, равнобедренным или равносторонним.
"""


def triangle():
    def t_i():
        return int(input('Input number: '))

    a, b, c = t_i(), t_i(), t_i()
    if a + b > c and a + c > b and b + c > a:
        if a == b and b == c:
            add = 'равносторонний'
        elif a == b or a == c or b == c:
            add = 'равнобедренный'
        else:
            add = 'разносторонний'
        return f"Треугольник существует и он {add}"
    else:
        return "Треугольника не существует"


print(triangle())
