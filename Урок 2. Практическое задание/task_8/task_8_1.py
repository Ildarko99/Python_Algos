"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? - 2
Какую цифру считать? - 3
Число 1: 223
Число 2: 21
Было введено 1 цифр '3'

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""


def counter():
    def mini_counter(digit, element):
        result = 0
        for num in str(digit):
            if int(num) == element:
                result += 1
        return result

    cnt = int(input('Сколько будет чисел: '))
    element = int(input('Какую цифру считать: '))
    res = 0
    numbers = 1
    while cnt != 0:
        res += mini_counter(int(input(f'Число {numbers}: ')), element)
        cnt -= 1
        numbers += 1
    print(res)


counter()
