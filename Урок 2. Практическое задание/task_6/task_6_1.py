"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ ЦИКЛ
"""
import random


def guessing():
    try_count = 0
    digit = random.randint(1, 101)
    user_try = int(input('Guess a digit from 1 to 100: '))
    counter = 1
    while user_try != digit:
        if user_try < digit:
            print('The digit is bigger')
        elif user_try > digit:
            print('The digit is smaller')
        user_try = int(input('Guess a digit from 1 to 100: '))
        counter += 1
        if counter == 10 and user_try != digit:
            return print(f'Это было число {digit}')
    print('You are right!')

guessing()