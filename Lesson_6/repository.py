"""Репозиторий (скрипт управления хранилищем данных)"""

from sqlalchemy.orm import sessionmaker
from models_db import Category, Unit, Position, Good, Employee, Vendor, engine
from data import CATEGORIES, UNITS, POSITION, GOODS, EMPLOYEE, VENDORS


class Repository:
    """создание сессии"""
    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.Session.configure(bind=engine)
        self.session = self.Session()
        
    def create_object_from_list(self, table_cls, *args):
        """добавление объектов в таблицу из списка"""
        for item in args[0]:
            if table_cls in (Unit, Position):
                self.create_object(table_cls, item[0])
            elif table_cls in (Category, Employee):
                self.create_object(table_cls, item[0], item[1])
            elif table_cls is Good:
                self.create_object(table_cls, item[0], item[1], item[2])
            elif table_cls is Vendor:
                self.create_object(table_cls, item[0], item[1], item[2], item[3], item[4])
            else:
                print('не известная модель!')
                self.session.rollback()

    def create_object(self, table_cls, *args):
        """добавление объекта в таблицу"""
        if table_cls in (Unit, Position):
            object_table = table_cls(args[0])
        elif table_cls in (Category, Employee):
            object_table = table_cls(args[0], args[1])
        elif table_cls is Good:
            object_table = table_cls(args[0], args[1], args[2])
        elif table_cls is Vendor:
            object_table = table_cls(args[0], args[1], args[2], args[3], args[4])
        else:
            print('не известная модель!')
            self.session.rollback()
        self.session.add(object_table)
        self.session.commit()
        
    def get_table_data(self, table_cls):
        """прочитать все данные из таблицы"""
        return self.session.query(table_cls).all()
    
    def get_by_key(self, table_cls, key):
        """получить данные по id"""
        return self.session.query(table_cls).get(key)
    
    def delete_by_key(self, tbl_cls, key):
        """удалить данные по id"""
        obj = self.session.query(tbl_cls).get(key)
        if obj:
            self.session.delete(obj)
            self.session.commit()

    def clear_table(self, tbl_cls):
        """очистить таблицу"""
        self.session.query(tbl_cls).delete()
        self.session.commit()





if __name__ == '__main__':
    REP = Repository()
    
    """наполнение по одному объекту в таблицу"""
    REP.create_object(Category, 'плитка', 'плитка наполная')
    REP.create_object(Unit, 'шт.')
    REP.create_object(Position, 'директор')
    REP.create_object(Good, 'Плитка напольная KeramoMarazzi', 3, 5)
    REP.create_object(Employee, 'Иванов Иван Петрович', 1)
    REP.create_object(Vendor, 'Карат', 'ОOO', 'Россия,Москва,ул.9мая, дом 13',
                      '+79693632514', '123@mail.ru')
    
    """наполнение данными таблицы из списка"""
    REP.create_object_from_list(Category, CATEGORIES)
    REP.create_object_from_list(Unit, UNITS)
    REP.create_object_from_list(Position, POSITION)
    REP.create_object_from_list(Good, GOODS)
    REP.create_object_from_list(Employee, EMPLOYEE)
    REP.create_object_from_list(Vendor, VENDORS)
    
    """прочитать все данные из таблицы"""
    REP.get_table_data(Good)

    """получить данные по id"""
    REP.get_by_key(Good, 4)

    """удалить данные по id"""
    REP.delete_by_key(Good, 4)

    """очистить таблицу"""
    REP.clear_table(Category)
    REP.clear_table(Unit)
    REP.clear_table(Position)
    REP.clear_table(Good)
    REP.clear_table(Employee)
    REP.clear_table(Vendor)