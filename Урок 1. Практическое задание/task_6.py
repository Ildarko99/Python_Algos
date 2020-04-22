"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

Пример:
Введите номер буквы: 4
Введёному номеру соответствует буква: d

Подсказка: используйте ф-ции chr() и ord()
"""


def my_order():
    import string
    x = int(input('Input number between 1 and 26: '))
    text = string.ascii_lowercase
    return f'It is number of "{text[x - 1]}" letter.'


print(my_order())
