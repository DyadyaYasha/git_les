"""
name - название пакета
version - версия(состоит из 3-х цифр)
description - краткое описание пакета
url - url адрес сайта
license - Лицензия (требуется верная запись!)
author - Имя автора
author_email - Почта автора
packages - Паеты, которые необходимо скопировать без рекурсии, необходимо указывать вложенные
py_modules - Модули которые неоходимо скопировать
install_requires - прямые зависимости пакета от других пакетов
scripts - запускаемые из командной строки скрипты
"""

from setuptools import setup # стандартный пакет

setup(
    name='mega-math',
    version='1.0.0',
    description='Collection of mathematical formulas.',
    url='https://github.com/DyadyaYasha/git_les',
    license='Apache License 2.0'
    author='DyadyaYasha'
    author_email='dyadyayasha@gmail.com'
    packages=[
        'mega-math' #вложения перечесляются через точку
    ]


)
