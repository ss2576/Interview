"""
4. Реализовать возможность переустановки значения цены товара.

Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса
и функцию дочернего (функция,
отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Наименование товара: {self.name}. Цена товара: {self.price} рублей.'


def main():
    try:
        name = input('Введите наименование товара:\n')
        price = int(input('Введите цену товара\n'))
        item = ItemDiscount(name, price)
        item_rep = ItemDiscountReport(name, price)
        print(item_rep.get_parent_data())
        new_price = int(input('Введите новую цену товара\n'))
        item.price = new_price
        item_rep.price = new_price
        print(item.price == item_rep.price == new_price)
        print(item_rep.get_parent_data())
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()