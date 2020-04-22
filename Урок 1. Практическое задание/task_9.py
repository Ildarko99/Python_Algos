"""
Задание 9.	Вводятся три разных числа. Найти, какое из них является средним
(больше одного, но меньше другого).

Подсказка: можно добавить проверку, что введены равные числа
"""


def three_numbers():
    def t_i():  # take_input
        return input('Input number: ')

    a, b, c = t_i(), t_i(), t_i()
    if a != b and a != c and b != c:
        if (a < b < c) or (c < b < a):
            return b;

            # Checking for a
        if (b < a < c) or (c < a < b):
            return a

        else:
            return c
    else:
        return 'Put correct numbers'


print(three_numbers())
