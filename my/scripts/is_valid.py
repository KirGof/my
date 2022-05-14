def is_valid(number):
    """ Проверка числа на уникальность. Все 4 цифры
    числа должны быть разные """

    try:
        # переводим наше число в список из символов. сравниваем с множеством.
        # (в множестве нет повторяющихся символов)
        number_list = list(str(number))
        if len(set(number_list)) == 4:
            return True
        return False

    except:
        return False