"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

Пример:

Задайте количество строк в матрице: 3
Задайте количество столбцов в матрице: 4
 36 20 42 38
 46 27  7 33
 13 12 47 15
[13, 12, 7, 15] минимальные значения по столбцам
Максимальное среди них = 15
"""
import random

rows = int(input('Задайте количество строк в матрице:\n'))
columns = int(input('Задайте количество столбцов в матрице:\n '))
MATRIX = []
for r in range(rows):
    row = []
    for el in range(columns):
        row.append(random.randrange(10, 100))
    MATRIX.append(row)
for r in MATRIX:
    print(r, end='\n')
minimums = [MATRIX[x][0] for x in range(rows)]
print(minimums)

for row in range(rows):
    for column_el in range(columns):
        if MATRIX[row][column_el] < minimums[column_el]:
            minimums[column_el] = MATRIX[row][column_el]


print(f'{minimums} - минимальные значения по столбцам \n'
      f'максимальное среди них {max(minimums)}')