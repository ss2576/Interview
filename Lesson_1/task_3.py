"""
Задание 3.	Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации
(нуль необходимо исключить). Заполнить этими данными список и словарь.
Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря.

Пример:
(
[18, 22, 21, 23, 18, 21, 19, 16, 18, 8],
{'elem_18': 18, 'elem_22': 22, 'elem_21': 21, 'elem_23': 23, 'elem_19': 19, 'elem_16': 16, 'elem_8': 8}
)
"""

import random


def random_number_generator(start, end, number_of_digits):
    result = []
    if start > end:
        start, end = end, start
    for digit in range(number_of_digits):
        number = random.randint(start, end)
        if (number == 0) or (number in result):
            continue
        result.append(number)
    sort_result = sorted(result)
    return sort_result


def creating_dictionary(sort_result):
    dictionary = {}
    for number in range(len(sort_result)):
        key = f'elem_{sort_result[number]}'
        dictionary[key] = sort_result[number]
    return dictionary


def main():
    try:
        start = int(input('Введите начальное число:\n'))
        end = int(input('Введите конечное число: \n'))
        number_of_digits = int(input('Введите количество случайных цифр: \n'))
        sort_result = random_number_generator(start, end, number_of_digits)
        dictionary = creating_dictionary(sort_result)
        print(sort_result)
        print(dictionary)
    except ValueError:
        print('Необходимо ввести натуральное число!')
        main()


if __name__ == '__main__':
    main()
