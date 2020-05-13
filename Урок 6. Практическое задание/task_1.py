"""
1.	Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.


ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""

"""
Сравним два метода поиска квадратов четных чисел.
Обычным способом и с помощью генераторов. И замерим выделяемый объем памяти.
"""

"""  Сначала проверим обычным способом"""
import memory_profiler
import time


def check_even1(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num * num)
    return even


m1 = memory_profiler.memory_usage()
t1 = time.clock()
cubes = check_even1(range(10_000_000))

res = 0
for i in cubes:
    res += i
print(res)

t2 = time.clock()
m2 = memory_profiler.memory_usage()
time_diff = t2 - t1
mem_diff = m2[0] - m1[0]

print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")

del res
del cubes

""" Теперь проверим с помощью генератора """
import memory_profiler
import time


def check_even2(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num * num


m1 = memory_profiler.memory_usage()
t1 = time.clock()
cubes = check_even2(range(10_000_000))
res = 0
for i in cubes:
    res += i
print(res)
t2 = time.clock()
m2 = memory_profiler.memory_usage()
time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f"It took {time_diff} Secs and {mem_diff} Mb to execute this method")

"""
Вывод:
в первом варианте мы задействуем 193 Мб памяти, во втором практически 0. 
Использование генераторов вместо хранения информации в списках существенно снижает 
использование памяти и их следует использовать при наличии возможности. 
Python 3.6, Ubuntu x64 
"""
