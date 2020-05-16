"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import timeit
import random

quicks = []
def bubble_sort(orig_list, sort=0):
    n = 1
    while n < len(orig_list):
        for i in range(len(orig_list) - n):
            if orig_list[i] < orig_list[i + 1]:
                orig_list[i], orig_list[i + 1] = orig_list[i + 1], orig_list[i]
                sort += 1

        if sort == 0: #эта операция добавляет возможность досрочно выйти, если не выполнялось сортировок
            quicks.append(1)
            return orig_list
        n += 1
        sort = 0
    return orig_list

print(len(quicks))
orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1000))
"""
Замеры без добавления выхода в случае прохода 
без единой сортировки в диапазонах, время в сек:
10   - 0.01192141100182198
100  - 0.6471109380072448
1000 - 69.05578172300011

Замеры с добавлением выхода в случае прохода 
без единой сортировки в диапазонах, время в сек:
10   - 0.0019351009977981448
100  - 0.021690814988687634
1000 - 0.2901765459973831

"""