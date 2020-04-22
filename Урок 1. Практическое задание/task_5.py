"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""
import string


def your_letters(a, b):
    text = string.ascii_lowercase
    a_index = text.find(a)
    b_index = text.find(b)
    if text.find(a) < text.find(b):
        section = text[a_index + 1:b_index]
        qty = text.find(b) - text.find(a) - 1
    else:
        text = text[::-1]
        section = text[b_index + 1:a_index]
        qty = text.find(a) - text.find(b) + 1
    return f'Your places is {a_index + 1}, {b_index + 1}, and there are {abs(qty)} letters between them.'


print(your_letters('a', 'f'))
print(your_letters('g', 'a'))
