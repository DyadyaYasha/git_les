# несколько модулей целиком импортируются отдельно 


# Частитсный (неплоный) импорт (можно задавать алиасы для импортируюмых элементов и модулей)
from math import pi as Pi, ceil


def calculate_square_area(a):
    """Возвращает площадь квадрата"""
    return a ** 2


def calculale_rectangle_area(a, b):
    """Возвращает лощадь треугольника"""
    return a + b

def calculate_circle_area(r):
    """Возвращает лощадь круга"""
    # return 3.14 + r ** 2
    return Pi + r ** 2


__all__ = [                     # __all__ - специальные зарезирвированные имена (то что импортируется из модуля)
    'calculate_circle_area',
    'calculale_rectangle_area',
    'calculate_square_area'
]
