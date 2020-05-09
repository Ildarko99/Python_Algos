"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
import time

# решение работает при i <= 6400
import timeit

print('='* 50)
print(f'start testing v.1')

def eratosphene(n):
    # n число, до которого хотим найти простые числа
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n + 1, number):
                numbers[candidate - 2] = 0
    result = list(filter(lambda x: x != 0, numbers))
    return result


def i_eratosphene(i):
    start = time.time()
    print(f'answer is {eratosphene(i*10)[i]}')
    finish = time.time()
    print(f'time {round((finish - start), 5)} sec')

i_eratosphene(10)
i_eratosphene(100)
i_eratosphene(1000)
i_eratosphene(5000)

print(f'end of testing v.1')
print('='*50)
print('='*50)
print(f'start testing v.2')
def second_erat(i): # здесь будем использовать алгоритм, построенный на генераторах
    start = time.time()
    s = [x for x in range(2, i*10+1) if x not in [i for sub in [list(range(2 * j, i*10+1, j)) for j in range(2, i*10 // 2)] for i in sub]]
    finish = time.time()
    print(f'answer is {s[i]}')
    print(f'time {round((finish - start), 5)} sec')

second_erat(10)
second_erat(100)
second_erat(200)
print(f'end of testing v.2')
print('='*50)
'''
Результаты замеров для чисел:
      |v1(for loops)  | v2(generators)
10    |7e-05 sec      |   0.0116 sec
100   |0.00057 sec    |   0.83496 sec
1000  |0.00619 sec    |   4.38362 sec

в варианте 2, построенном на генераторе, четыре уровня вложенных цикла for, что дает оценку сложности O(n^4)
против O(n^2) в первом случае. На малых значениях (до i<= 10) второй вариант жизнеспособен, но далее время работы 
увеличивается в прогрессии, что делает его совершенно нерабочим
'''