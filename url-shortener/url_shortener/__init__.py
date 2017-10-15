import os.path as Path # позволяет работать с файловой системой
import sys

from url_shortener import storage

get_connection = lambda : storage.connect('shortener.sqlite') # lambda автоматически возвращает соединение

def action_add():
    """Добавить url-адрес"""
    url = input('\nВведите URL-адрес: ')

    with get_connection() as conn:
        short_url = storage.add_url(conn, url)

    print('Короткий адрес: {}'.format(short_url))
    # если мы отрицаем пустоту т.е. not то возвращаем истину

    if not url:
        return


def action_find():
    """Найти оригинальный url-адрес"""
    short_url = input('Введите короткий URL-адрес: ')
    # kлюбую введённую строчку можно привести к истене, пустой ввод игнорируется
    if short_url:
        with get_connection() as conn:
            row = storage.find_url_by_short(conn, short_url)

        if row:
            url = row.get('original_url')
            print('Оригинальный URL-адрес: {}'.format(url)) # format вставляет то что нам нужно в {}
        else:
            print('Короткий url-адрес "{}" не существует'.format(short_url))



def action_find_all():
    """Вывести все url-адреса"""
    with get_connection() as conn:
        rows = storage.find_all(conn)

    template = '{row[short_url]} - {row[original_url]} - {row[created]}' # если проименовать значения то можно подставить квадратные скобки в которые format вытащит из словаря нужные данные
    # дату можно еще форматироать в удобный вид
    # можно нумеровать template = '{0} - {0} - {1}' тогда format нужно передать всего 2 аргумента

    for row in rows:
        print(template.format(row=row))

def action_show_menu():
    """Показать меню"""
    print("""
1. Добавить URL-адрес
2. Найти оригинальный URL-адрес
3. Вывести все URL-адреса
m. Показать меню
q. Выйти""")


def action_exit():
    """Выйти из программы"""
    sys.exit(0)


def main():
    creation_schema = Path.join( # склеивает путь файла с разделитилем определённой OS
        Path.dirname(__file__), 'schema.sql' # позволяет вернуть родительскую директорию файла и отрежет файл оставив только путь
    )

    with get_connection() as conn:
        storage.initialize(conn, creation_schema)

    actions = {
        '1': action_add,
        '2': action_find,
        '3': action_find_all,
        'm': action_show_menu,
        'q': action_exit
    }

    action_show_menu()
# метод get не завершит программу при ошибочном вводе, он обрезает ошибочный ввод 
    while True:
        cmd = input('\n Введите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')