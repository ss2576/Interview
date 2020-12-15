"""
Задание 2.	Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):

    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    заполните далее

Пример:
[
('mainapp', 'admin.py'),
('mainapp\\management\\commands', 'seed_db.py'),
...
]
"""

import os


def print_directory_contents(sPath):
    try:
        dirs = []
        dirs_full = []
        files = []
        for path in os.listdir(sPath):
            full_path = os.path.join(sPath, path)
            if os.path.isdir(full_path):
                dirs.append(path)
                dirs_full.append(full_path)
            else:
                files.append(path)
        data = (sPath, dirs, files)
        print(data)
        for dir in dirs_full:
            print_directory_contents(dir)
            
    except FileNotFoundError as e:
        print(e.args, sPath)
        main()


def main():
    sPath = input('Введите директорию: \n')
    print_directory_contents(sPath)


if __name__ == '__main__':
    main()
