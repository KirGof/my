from scripts.check import check
from scripts.is_valid import is_valid
from scripts.game import game
import random


def main():

    # переменные
    number_guess, number_computer, n = 0, 0, 0

    # списки
    n_c, n_b = [], []


    # генерируем число, которое нужно отгадать
    while not is_valid(number_guess):
        number_guess = random.randint(1000, 9999)

    # генерируем число от которого наша программа будет отталкиваться
    while not is_valid(number_computer):
        number_computer = random.randint(1000, 9999)

    print(number_guess, number_computer)

    # главный цикл, работает, пока не будет 4 быка, то есть
    # два числа не будут ровны между собой

    # получаем списки индексов коров и быков
    n_c, n_b = check(number_guess, number_computer)

    while len(n_b) != 4:
        # пересобираем число из имеющихся данных
        number_guess = game(number_guess, n_c, n_b)

        # получаем списки индексов коров и быков
        n_c, n_b = check(number_guess, number_computer)
        n += 1
        print(f"Попытка: {n}; Число: {number_guess}; Число, которое нужно отгадать: {number_computer}")

    print(number_guess)


if __name__ == '__main__':
    main()
