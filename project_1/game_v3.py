"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def dichotomy_predict(number: int = 1) -> int:
    """Угадываем число от 1 до 100 дихотомическим делением

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    num_min = 0  # минимальное возможное число
    num_max = 100  # максимальное возможное число

    while True:
        count += 1
        predict_number = (num_min + num_max)//2 + \
                         (num_min + num_max) % 2  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
        elif predict_number < number:
            num_min = predict_number  # вдвое сокращаем интервал поиска снизу
        else:
            num_max = predict_number  # вдвое сокращаем интервал поиска сверху

    return count


def score_game(dichotomy_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов
       угадывает наш алгоритм

    Args:
        dichotomy_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(dichotomy_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(dichotomy_predict)
