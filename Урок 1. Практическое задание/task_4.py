"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

# до примечания добрался уже после того, как все сделал. Сделал только с помощью random(), но со списками
import random


def my_random(start=None, stop=None):
    from random import random
    import string
    text = string.ascii_lowercase
    elements = []
    if isinstance(start, int) and isinstance(stop, int):  # проверяем, что пользователь хочет число, а не символы
        if start <= stop:
            for el in range(int(start), int(stop)):
                elements.append(el)
        else:
            for el in range(int(stop), int(start)):
                elements.append(el)
        if not elements:
            return 0
        multiplier = int('1' + '0' * len(str(len(elements))))
        # вычисляем порядок числа множителя для рандома, сколько
        # оставить знаков в числе до точки

        index = int(random() * multiplier)  # вычисляем рандомный индекс элемента в списке
        while index >= len(elements):  # проверяем, входит ли рандомный индекс в нужный диапазон. Перебираем до нужного.
            index = int(random() * multiplier)
        return f'Your random digit is: {elements[index]}'
    elif isinstance(start, str) and isinstance(stop, str):
        if text.find(start) < text.find(stop):
            section = text[text.find(start) + 1: text.find(stop)]
        else:
            text = text[::-1]
            section = text[text.find(start) + 1: text.find(stop)]
        multiplier = int('1' + '0' * len(str(len(section))))
        index = int(random() * multiplier)  # вычисляем рандомный индекс элемента в списке
        while index >= len(section):  # проверяем, входит ли рандомный индекс в нужный диапазон
            index = int(random() * multiplier)
        return f'Your random symbol is: {section[index]}'
    else:
        multiplier = 100
        index = int(random() * multiplier)
        while index >= len(text):  # проверяем, входит ли рандомный индекс в нужный диапазон
            index = int(random() * multiplier)
        return f'Your random symbol is: {text[index]}'


import string

text = string.digits
print(text)
print(my_random(0, 10))
for i in range(1000):
    print(my_random(int(random.choice(text)), int(random.choice(text))))
print(my_random(-1000, 1000))
print(my_random(100, -100))
print(my_random('a', 'f'))
print(my_random('f', 'a'))
print(my_random())


def another_random(a, b):
    import random
    return random.randrange(a, b)


print(another_random(1, 10))

