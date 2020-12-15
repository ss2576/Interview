"""
5. Реализовать расчет цены товара со скидкой.

Величина скидки должна передаваться в качестве аргумента в дочерний класс.

Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.

В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой.

Чтобы все работало корректно, не забудьте инициализировать дочерний
и родительский классы
(вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.__discount = discount

    def __str__(self):
        return f'Наименование товара: {self.name}. Цена товара со скидкой: {self.price - self.price * self.__discount / 100} руб.'

    def get_parent_data(self):
        return f'Наименование товара: {self.name}. Цена товара: {self.price} руб.'
        

def main():
    try:
        name = input('Введите наименование товара:\n')
        price = int(input('Введите цену товара\n'))
        discount = int(input('Введите процент скидки\n'))
        item_rep = ItemDiscountReport(name, price, discount)
        print(item_rep.get_parent_data())
        print(item_rep)
    except Exception as e:
        print(f'{type(e).__name__}: {e}')


if __name__ == '__main__':
    main()