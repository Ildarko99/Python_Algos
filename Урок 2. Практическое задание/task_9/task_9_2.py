"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите число: 23
Введите число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""

def counter():
    def calc(num):
        if num == 0:
            return 0
        return num % 10 + calc(num // 10)
    cnt = int(input('Введите количество чисел: '))
    max, res = 0, 0
    while cnt != 0:
        new = int(input('Введите число: '))
        summ_of_new = calc(new)
        if max > summ_of_new:
            continue
        else:
            max = summ_of_new
            res = new
        cnt -= 1
    return f'Наибольшее число по сумме цифр: {res}, сумма его цифр: {max}'


print(counter())