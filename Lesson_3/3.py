"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""

from itertools import zip_longest


def generate_array(pref, size):
    return [f'{pref}_{i}' for i in range(size)]


def main():
    keys = generate_array('key', int(input('введите длину списка ключей:\n')))
    values = generate_array('values', int(input('введите длину списка значений:\n')))
    result = {key: value for key, value in zip_longest(keys, values) if key}
    print(f'список ключей:\n {keys} \n список значений:\n {values} \n получили словарь:\n {result}')


if __name__ == '__main__':
    main()