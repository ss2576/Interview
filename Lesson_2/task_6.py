"""
6. Проверить на практике возможности полиморфизма.

Необходимо разделить дочерний класс ItemDiscountReport на два класса.

Инициализировать классы необязательно.

Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены.

Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemDiscountReportName(ItemDiscount):

    def get_info(self):
        return self.name

    @staticmethod
    def get_info_st(item):
        return item.name


class ItemDiscountReportPrice(ItemDiscount):

    def get_info(self):
        return self.price

    @staticmethod
    def get_info_st(item):
        return item.price


def main():
    try:
        name = input('Введите наименование товара:\n')
        price = int(input('Введите цену товара\n'))
        item = ItemDiscount(name, price)
        item_rep_name = ItemDiscountReportName(name, price)
        item_rep_price = ItemDiscountReportPrice(name, price)
        items_array = [item_rep_name, item_rep_price]
        items_class_array = [ItemDiscountReportName, ItemDiscountReportPrice]

        print('способ №1')
        for _ in items_array:
            print(_.get_info())

        print('способ №2')
        print(item_rep_name.get_info())
        print(item_rep_price.get_info())

        print('способ №3')
        for _ in items_class_array:
            if hasattr(_, 'get_info_st'):
                print(getattr(_, 'get_info_st')(item))

    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()