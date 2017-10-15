import os.path as Path
import sqlite3

from .converter import convert, inverse # относительный импорт

SQL_SELECT_ALL = """
    SELECT id, original_url, short_url, created
    FROM shortener
"""

SQL_SELECT_URL_BY_PK = SQL_SELECT_ALL + " WHERE id=?"

SQL_SELECT_URL_BY_ORIGINAL = SQL_SELECT_ALL + " WHERE original_url=?"

SQL_SELECT_URL_BY_SHORT = SQL_SELECT_ALL + " WHERE short_url=?"

SQL_INSERT_URL = """
    INSERT INTO shortener (original_url) VALUES (?)
"""

SQL_UPDATE_SHORT_URL = """
    UPDATE shortener SET short_url=? WHERE id=?
"""
# обязательно условие WHERE и то что должно обновиться, без него обновится все в таблице

def dict_factory(cursor, row):
    d = {}

    print('===> Row', row)
    print('===>', cursor.description)

    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]


    return d


def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    # магия
    conn.row_factory = dict_factory

    return conn

def initialize(conn, creation_schema):
    with conn, open(creation_schema) as f: # отдаём открытое соединение, with не будет его закрывать, т.к. не открывал его
        conn.executescript(f.read()) # executescript - выполняет кучу запросов разбивая запросы по ;


def add_url(conn, url, domain=''):
    """ Сохраняет новый url-адрес в базу"""
    url = url.strip('/')

    if not url:
        # здесь должна быть ошибка
        print('URL can not be empty')
        return
    with conn:
        found = find_url_by_original(conn, url)

        if found:
            return found.get('short_url')

        cursor = conn.execute(SQL_INSERT_URL, (url,))

        # последний сгенерированный запросом INSERT PK
        pk = cursor.lastrowid
        short_url = '{}/{}'.format(domain.strip('/'), convert(pk))
        conn.execute(SQL_UPDATE_SHORT_URL, (short_url, pk))
        return short_url


def find_all(conn):
    """Возвращает все url-адреса из базы"""
    with conn:
        cursor = conn.execute(SQL_SELECT_ALL) 
        return cursor.fetchall()


def find_url_by_pk(conn, pk):
    """Возвращает url-адрес по первичному ключу"""
    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_PK, (pk,))
        return cursor.fetchone() # возвратит одну строку из результата, если вызвать fetchone еще раз, то вернёт 2-ю строчку


def find_url_by_short(conn, short_url):
    """Возвращает url-адрес по короткому url-у"""
    short_url = short_url.rsplit('/', 1).pop() # rsplit('/', 1) режем с правого края по / и режем один раз
    pk = inverse(short_url) # запрос по первичному ключу намного быстрее чем обычный запрос
    return find_url_by_pk(conn, pk)

def find_url_by_original(conn, original_url):
    """Возвращает url-адрес по оригинальному url-у"""
    original_url = original_url.strip('/') # обрезает по бокам определённый нами символ

    with conn:
        cursor = conn.execute(SQL_SELECT_URL_BY_ORIGINAL, (original_url,))
        return cursor.fetchone()
