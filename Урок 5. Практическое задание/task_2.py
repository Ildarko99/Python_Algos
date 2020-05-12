"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from _collections import deque
from functools import reduce

# first, second = deque([el for el in input('Insert first: ').split()]), deque([el for el in input('Insert second: ').split()])
# first = list(input('Insert first:\n'))
# second = list(input('Insert second:\n'))
first = ['A', '2']
second = ['C', '4', 'F']

print(first, second)


def adding_in_16(first, second):
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    def letters_to_digits(x):
        for el in range(len(x)):
            if x[el] in letters:
                x[el] = letters[x[el]]
        return x

    def all_to_int(x):
        res = deque(map(lambda el: int(el), x))
        return res

    def filling_by_zeros(first, second):  # чтобы уравнять размеры списков,
        # проверяем их и наполняем первый нулями, в случае необходимости
        if len(first) >= len(second):
            while len(first) != len(second):
                second.appendleft(0)
        else:
            while len(first) != len(second):
                first.appendleft(0)
        return first

    def to_conditions(first, second):
        first = letters_to_digits(first)
        second = letters_to_digits(second)
        first = all_to_int(first)
        second = all_to_int(second)
        first = filling_by_zeros(first, second)
        return first, second

    first, second = to_conditions(first, second)

    def digits_to_letters(x):
        inv_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        for el in range(len(x)):
            if x[el] in inv_letters:
                x[el] = inv_letters[x[el]]
        return x

    def adding(first, second):
        result = deque([])
        p = 0
        for el in range(len(second) - 1, -1, -1):
            s = first[el] + second[el] + p
            p = 0
            if s > 16:
                p = s // 16
                s = s % 16
            elif s == 16:
                p = 1
                s = 0
            result.appendleft(s)
            if el == 0 and p != 0:
                result.appendleft(p)
        return digits_to_letters(result)

    return adding(first, second)


def multiplying_in_16(first, second):
    letters = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    def letters_to_digits(x):
        for el in range(len(x)):
            if x[el] in letters:
                x[el] = letters[x[el]]
        return x

    def all_to_int(x):
        res = deque(map(lambda el: int(el), x))
        return res

    def filling_by_zeros(first, second):  # чтобы уравнять размеры списков,
                                                # проверяем их и наполняем первый нулями, в случае необходимости
        if len(first) >= len(second):
            while len(first) != len(second):
                second.appendleft(0)
        else:
            while len(first) != len(second):
                first.appendleft(0)
        return first

    def to_conditions(first, second):
        first = letters_to_digits(first)
        second = letters_to_digits(second)
        first = all_to_int(first)
        second = all_to_int(second)
        # first = filling_by_zeros(first, second)
        return first, second

    first, second = to_conditions(first, second)

    def digits_to_letters(x):
        inv_letters = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        for el in range(len(x)):
            if x[el] in inv_letters:
                x[el] = inv_letters[x[el]]
        return x

    def ones_multiply(x, lst, flag):
        result = deque([])
        p = 0
        s = 0
        if flag != 0:
            for el in range(flag):
                result.append(0)
        for el in range(len(lst) - 1, -1, -1):
            s += x * lst[el] + p
            p = 0
            if s > 16:
                p = s // 16
                s = s % 16
            result.appendleft(s)
            s = 0
            if el == 0 and p != 0:
                result.appendleft(p)
        return result
#[deque([9, 7, 14]), deque([2, 8, 8]), deque([7, 9, 8])]
    def multiply(first, second):
        # result = deque([0 for el in range(len(first) * len(second))])
        prom_res = []
        flag = 0
        for el in range(len(second)-1, -1, -1):
            prom_res.append(ones_multiply(second[el], first, flag))
            flag += 1
        prom_res = map(lambda x: digits_to_letters(x), prom_res) #correct till this place
        result = reduce(lambda x, y: adding_in_16(x, y), prom_res)
        return result

    return multiply(first, second)


print(f'Summ = {adding_in_16(first, second)}')
print(f'Multiply = {multiplying_in_16(first, second)}')


