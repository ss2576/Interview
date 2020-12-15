"""
Проверить механизм наследования в Python.

Для этого создать два класса. Первый — родительский (ItemDiscount),
должен содержать статическую информацию о товаре: название и цену.

Второй — дочерний (ItemDiscountReport),
должен содержать функцию (get_parent_data), отвечающую
за отображение информации о товаре в одной строке.

Проверить работу программы.
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Наименование товара: {self.name}. Цена товара: {self.price} рублей.'


def main():
    name = input('Введите наименование товара:\n')
    price = int(input('Введите цену товара\n'))
    item_rep = ItemDiscountReport(name, price)
    print(item_rep.get_parent_data())


if __name__ == '__main__':
    main()