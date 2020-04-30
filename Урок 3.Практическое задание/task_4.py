"""
Задание_4. Определить, какое число в массиве встречается чаще всего

Подсказка: можно применить ф-цию max с параметром key
"""
import random

a = [random.randint(1, 100) for el in range(100)]
print(max(a, key=lambda x: a.count(x)))
