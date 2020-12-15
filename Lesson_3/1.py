"""
 Написать программу, которая будет содержать функцию для получения имени
  файла из полного пути до него. При вызове функции в качестве аргумента
  должно передаваться имя файла с расширением. В функции необходимо
   реализовать поиск полного пути по имени файла, а затем «выделение»
    из этого пути имени файла (без расширения).
"""

import os


def get_filename(file):
    full_path = os.path.abspath(file)
    file_name = os.path.basename(full_path)
    return os.path.splitext(file_name)[0]


def main():
    file = input('введите файл с расширением\n')
    print(get_filename(file))


if __name__ == '__main__':
    main()
