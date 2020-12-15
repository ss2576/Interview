"""
Написать программу, которая запрашивает у пользователя
ввод числа. На введенное число она отвечает сообщением,
целое оно или дробное. Если дробное — необходимо далее
выполнить сравнение чисел до и после запятой. Если они
совпадают, программа должна возвращать значение True, иначе False.
"""

import re


def check_number_type(num):
    if num.isdigit():
        print(f'{num} это целое число')
        return
    elif num.isalnum():
        print(f'{num} это не число')
        return
    else:
        print(f'{num} это дробное число')
        num = num.replace(',', '.')
        left_part, right_part = map(int, num.split('.'))
        return left_part == right_part


INT_REG_EXPRESS = r'\d+'
FL_REG_EXPRESS = r'\d+[.,]\d+'


def re_check_number_type(num):
    if re.fullmatch(INT_REG_EXPRESS, num):
        print(f'{num} это целое число')
        return
    elif re.fullmatch(FL_REG_EXPRESS, num):
        print(f'{num} это дробное число')
        num = num.replace(',', '.')
        left_part, right_part = map(int, num.split('.'))
        return left_part == right_part
    else:
        print(f'{num} это не число')
        return


def main():
    num = input('введите число\n')
    try:
        result = check_number_type(num)
        if result is not None:
            r_word = "равна" if result else "не равна"
            print(f'левая часть {r_word} правой части')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()