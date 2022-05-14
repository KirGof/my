def check(number_guess, number_computer):
    """ Находим количество коров и быков в числе """

    # индексы коров и быков
    n_c, n_b = [], []

    try:
        # переводим наши числа в список из символов.
        number_guess_list = list(str(number_guess))
        number_computer_list = list(str(number_computer))

        # проходимся по числ
        for index in range(len(number_guess_list)):

            # если в разных числа в одинаковых индексах цифры ровны, то это бык
            if number_computer_list[index] == number_guess_list[index]:
                n_b.append(index)
            # если в числах есть одинаковые цифры, но на разных местах, то это корова
            elif number_guess_list[index] in number_computer_list:
                n_c.append(index)

        # возвращаем списки индексов коров и быков
        return n_c, n_b

    except:
        return n_c, n_b
