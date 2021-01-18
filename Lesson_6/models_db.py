"""Шаблоны таблиц (модели) БД"""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

# Используем стильный декларативный подход
Base = declarative_base()
engine = create_engine('sqlite:///database.sqlite3', echo=False)


def get_repr(obj):
    fiels = obj.__mapper__.attrs.keys()
    fiels_str = ', '.join([f'{fld}={getattr(obj, fld)}' for fld in fiels])
    return f'<{obj.__class__.__name__}({fiels_str})>'


class Category(Base):
    """Категории товаров"""
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String(50), nullable=False)
    category_description = Column(String(200), nullable=False)

    def __init__(self, name, desc):
        self.category_name = name
        self.category_description = desc

    def __repr__(self):
        return get_repr(self)


class Unit(Base):
    """Единицы измерения товара"""
    __tablename__ = 'units'
    unit_id = Column(Integer, primary_key=True)
    unit = Column(String(10), nullable=False)

    def __init__(self, unit):
        self.unit = unit

    def __repr__(self):
        return get_repr(self)


class Position(Base):
    """Должности"""
    __tablename__ = 'positions'
    position_id = Column(Integer, primary_key=True)
    position = Column(String(20), nullable=False)

    def __init__(self, position):
        self.position = position

    def __repr__(self):
        return get_repr(self)


class Good(Base):
    """Товары"""
    __tablename__ = 'goods'
    good_id = Column(Integer, primary_key=True)
    good_name = Column(String(50), nullable=False)
    good_unit = Column(Integer, ForeignKey('units.unit_id'))
    good_cat = Column(Integer, ForeignKey('categories.category_id'))

    def __init__(self, name, unit, cat):
        self.good_name = name
        self.good_unit = unit
        self.good_cat = cat

    def __repr__(self):
        return get_repr(self)


class Employee(Base):
    """Сотрудники"""
    __tablename__ = 'employees'
    employee_id = Column(Integer, primary_key=True)
    employee_fio = Column(String(50), nullable=False)
    employee_position = Column(Integer, ForeignKey('positions.position_id'))

    def __init__(self, fio, position):
        self.employee_fio = fio
        self.employee_position = position

    def __repr__(self):
        return get_repr(self)


class Vendor(Base):
    """Поставщики"""
    __tablename__ = 'vendors'
    vendor_id = Column(Integer, primary_key=True)
    vendor_name = Column(String(50), nullable=False)
    vendor_owner_chip_form = Column(String(50), nullable=False)
    vendor_address = Column(String(200), nullable=False)
    vendor_phone = Column(String(20), nullable=False)
    vendor_email = Column(String(20), nullable=False)

    def __init__(self, name, ownerchipform, address, phone, email):
        self.vendor_name = name
        self.vendor_owner_chip_form = ownerchipform
        self.vendor_address = address
        self.vendor_phone = phone
        self.vendor_email = email

    def __repr__(self):
        return get_repr(self)
    
    
Base.metadata.create_all(engine)

