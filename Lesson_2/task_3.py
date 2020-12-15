"""
3. Усовершенствовать родительский класс таким образом,
чтобы получить доступ к защищенным переменным.
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


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        return f'Наименование товара: {self.name}. Цена товара: {self.price} рублей.'


def main():
    try:
        name = input('Введите наименование товара:\n')
        price = int(input('Введите цену товара\n'))
        item_rep = ItemDiscountReport(name, price)
        print(item_rep.get_parent_data())
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()