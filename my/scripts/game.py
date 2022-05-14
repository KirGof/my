import random
from scripts.is_valid import is_valid


def game(number_guess, n_c, n_b):
    """ Ф-я, пересобирания числа из имеющихся данных """

    # переводим наше число в список из символов
    number_guess_list = list(str(number_guess))

    # проходимся по списку number_guess_list
    for index in range(len(number_guess_list)):
        # если индекса цифры нет в списке индексов быков,
        # но есть в в списке коров
        if index not in n_b and index in n_c:
            # рандомным способом переставляем
            index_random = n_c[random.randint(0, len(n_c)-1)]
            number_guess_list[index], number_guess_list[index_random] = number_guess_list[index_random], number_guess_list[index]
        # если индекса цифры нет ни в одном из списков
        if index not in n_b and index not in n_c:
            number_guess_list[index] = str(random.randint(1, 9))
            while not is_valid(int(''.join(number_guess_list))):
                number_guess_list[index] = str(random.randint(1, 9))

    return int(''.join(number_guess_list))