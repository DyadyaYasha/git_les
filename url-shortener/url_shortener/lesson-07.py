"""
SQL - стандартный язык запроса (Standart Query Language)
- DDL - Data Definition Language (Язык описания данных)
    (CREATE TABLE - создаёт таблицу)
- DML - Data Manipulatio Language (Язык манипуляции данных)
    (SELECT - выборка данных, INSERT - вставка данных, UPDATE - обновляет существующие данные, DELETE)

СУБД - система управления базами данных
Primary Key (Первичный ключ)
    Уникальный идентификатор 
    PK (PRIMARY KEY) - уникальный ключ (может быть int, str, составной(суррогатный))
Foreign Key - внешний ключ (для связи между двумя таблицами)

Алгоритм работы с БД:
1. Установка соединения .connect()
2. Создани объекта курсора .cursor()
3. Выполнение SQL-запроса(ов) cursor.execute()
4. Если запрос изменяет данные/структуру
    4.1 зафиксировать изменения conn.commit()
4. Если запрос на выборку/получения данных
    4.1 разобрать данные (fetch*)
"""

# SQLite3 - база данных в одном файле (не СУБД)

import sqlite3 # современная версия

#conn = sqlite3.connect(':memory:') # для теста делаем базу данных в оперативной памяти :memory:
conn = sqlite3.connect('users.sqlite') # програмка для просмотра sqlite browser

cursor = conn.cursor()

# создаём таблицу (id - название колонки, INTEGER - тип данных, PRIMARY KEY - (атрибут)уникальное поле, AUTOINCREMENT )
# IF NOT EXISTS - создать таблицу если её нет
# после запятой, на следующей строчке пишем следующую колонку
# СУБД не любит пустые колонки (None) - работают они медленно
# NOT NULL - обязательное заполнение колонки
# DEFAULT - значение поумолчанию
# CURRENT_TIMESTAMP - текущее время (время создания)
# 
sql = """
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
"""

cursor.execute(sql)

conn.commit() # изменения зафиксированны

# создане запроса

sql = """
    INSERT INTO user (
        firstname, lastname
    ) VALUES (
        ?, ? 
    )
"""

# выполняем запрос

cursor.execute(sql, (input(), input())) # execute принимает один аргумент - кортеж () (('',)) - именно в таком формате
conn.commit()

# вытаскиваем Васю Пупкина из базы

sql = """
    SELECT id, firstname, lastname, created

    FROM user
"""
# выполняем запрос

cursor.execute(sql) # данные как-бы находятся в cursor

users = cursor.fetchall() # fetchall - вытаскивает все данные fetchone - вытаскивает по одной записи

print(users)

conn.close()

# использую контексный менеджер, всё можно сократить

with sqlite3.connect('users.sqlite') as conn:
    # cursor = conn.cursor()
    # cursor.execute()
    cursor = conn.execute(sql) # execute внутри себя создаёт cursor и возвращает его обратно
    users = cursor.fetchall()
    print(users)




