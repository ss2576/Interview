"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и
подготовить два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы.
Применить к спискам функцию zip(). Результат выполнения этой функции должен должен быть обработан и
записан в файл таким образом, чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

import os
import random
import string


ARR_SIZE = random.randint(15, 20)
WORD_LEN = random.randint(5, 15)
SEP = ' '
LAMBDA_EXPRESSION = lambda t: f'{t[0]}{SEP}{t[-1]}'


def generate_int_array(size):
    for i in range(size):
        yield random.randint(1, 100000)


def generate_str_array(size):
    for i in range(size):
        yield ''.join(random.choice(string.ascii_letters) for i in range(WORD_LEN))


def write_data(file):
    if os.path.isfile(file):
        print(f'{file} файл с таим именем существует,переписать его?')
        answer = input('Продожить (Y/n)?\n') or 'y'
        if answer.lower() != 'y':
            return

    int_arr = generate_int_array(ARR_SIZE)
    str_arr = generate_str_array(ARR_SIZE)
    zip_arr = zip(int_arr, str_arr)

    with open(file, 'w', encoding='utf-8') as writer:
        writer.write('\n'.join(map(LAMBDA_EXPRESSION, zip_arr)))
    read_file(file)


def read_file(file):
    with open(file, 'r', encoding='utf-8') as reader:
        content = reader.read().split('\n')
    for line in content:
        print(line)



def main():
    file = input('дайте имя файлу:\n') or 'file.txt'
    write_data(file)


if __name__ == '__main__':
    main()
