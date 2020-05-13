"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога

Предприятия, с прибылью ниже среднего значения: Копыта
"""
import collections
from statistics import mean
from memory_profiler import profile

# ====================================================================
# Реализация через словарь
@profile
def companies_by_colls_Counter():
    # lenght = int(input('Сколько будет компаний:\n'))
    COMPANIES = collections.Counter()
    # for i in range(lenght):
    #     comp = input(f'Компания {i + 1}: ')
    #     av = sum([int(i) for i in input(f'через пробел введите прибыль данного предприятия '
    #                                     f'за каждый квартал (Всего 4 квартала):\n').split()]) / 4
    COMPANIES['Luk'] = 50
    COMPANIES['Gaz'] = 20

    print(
        f'Средняя годовая прибыль всех предприятий: {mean(COMPANIES.values())}\n'  # с помощью mean выводим среднее значение итерируемого объекта
        f'Предприятия, с прибылью выше среднего значения: {max(COMPANIES.values())} - {max(COMPANIES, key=COMPANIES.get)}\n'
        f'Предприятия, с прибылью ниже среднего значения: {max(COMPANIES.values())} - {min(COMPANIES, key=COMPANIES.get)}')
    return COMPANIES


# ====================================================================
# Реализация через именованный кортеж


@profile()
def companies_by_nmtuple():
    # lenght = int(input('Сколько будет компаний:\n'))
    comps = ['Luk', 'Gaz']
    # for el in range(lenght):
    #     x = input(f'Компания {el + 1}: ')
    #     comps.append(x)
    c = collections.namedtuple('Company', comps)
    av = [50, 20]
    # for el in comps:
    #     x = sum([int(i) for i in input(f'Через пробел введите прибыль {el} '
    #                                    f'за каждый квартал (Всего 4 квартала):\n').split()]) / 4
    #     av.append(x)
    Company = c(*av)

    print(f'Средняя годовая прибыль всех предприятий: {mean(Company)}\n'
          f'Предприятия, с прибылью выше среднего значения: {max(Company)} - {Company._fields[Company.index(max(Company))]} \n'
          f'Предприятия, с прибылью ниже среднего значения: {min(Company)} - {Company._fields[Company.index(min(Company))]}')
    return Company


companies_by_colls_Counter()
companies_by_nmtuple()

"""

"""
import collections
from statistics import mean


# ====================================================================
# Реализация через словарь
def companies_by_colls_Counter():
    lenght = int(input('Сколько будет компаний:\n'))
    COMPANIES = collections.Counter()
    for i in range(lenght):
        comp = input(f'Компания {i + 1}: ')
        av = sum([int(i) for i in input(f'через пробел введите прибыль данного предприятия '
                                        f'за каждый квартал (Всего 4 квартала):\n').split()]) / 4
        COMPANIES[comp] = av

    print(
        f'Средняя годовая прибыль всех предприятий: {mean(COMPANIES.values())}\n'  # с помощью mean выводим среднее значение итерируемого объекта
        f'Предприятия, с прибылью выше среднего значения: {max(COMPANIES.values())} - {max(COMPANIES, key=COMPANIES.get)}\n'
        f'Предприятия, с прибылью ниже среднего значения: {max(COMPANIES.values())} - {min(COMPANIES, key=COMPANIES.get)}')
    return COMPANIES


# ====================================================================
# Реализация через именованный кортеж

def companies_by_nmtuple():
    lenght = int(input('Сколько будет компаний:\n'))
    comps = []
    for el in range(lenght):
        x = input(f'Компания {el + 1}: ')
        comps.append(x)
    c = collections.namedtuple('Company', comps)
    av = []
    for el in comps:
        x = sum([int(i) for i in input(f'Через пробел введите прибыль {el} '
                                       f'за каждый квартал (Всего 4 квартала):\n').split()]) / 4
        av.append(x)
    Company = c(*av)

    print(f'Средняя годовая прибыль всех предприятий: {mean(Company)}\n'
          f'Предприятия, с прибылью выше среднего значения: {max(Company)} - {Company._fields[Company.index(max(Company))]} \n'
          f'Предприятия, с прибылью ниже среднего значения: {min(Company)} - {Company._fields[Company.index(min(Company))]}')
    return Company


companies_by_colls_Counter()
companies_by_nmtuple()
