# Форматы данных 

# Pickle - нативный питоновский формат(прочитать можно только в Python)

import pickle # python2 =( -> six - позволяет писать совместимые программы как для python2 так и для python3

data = {
    'users': [
        {
        'id': 1,
        'name': 'Linus Torvalds',
        'skills': ('C++', 'C')
        },
        {
        'id': 2,
        'name': 'Richard Stallman',
        'skills': ('C', 'GNU')
        }
    ]
}

with open('users.pickle', 'wb') as f:
    pickle.dump(data, f) # (data - данные, f - открытый файл) dump - позволяет вернуть строчку и сразу же её записать в файл

with open('users.pickle', 'rb') as f:
    loaded_data = pickle.load(f)
    print(loaded_data)

# Json - JavaScript Oject Notation (для общения между серверами(на разных языказ программирования))

import json

with open('users.json', 'w') as f:
    json.dump(data, f)

with open('users.json') as f:
    print(json.load(f))

# CSV

import csv

"""
id;name;skills
1;Linus Torvalds;C,C++
2;Richard Stallman;C,GNU
"""

with open('user.csv', 'w') as f:
    users = data.get('users', []) # get (ключ есть, то возвращает значение под ключём, если нет то возвращает значение поумолчанию) - работает со словарём, если ключа в словаре нет, не получим ошибку а получим None
    fieldnames = users[0].keys() # !!!!

    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer = csv.DictWriter(f, 
    #                         fieldnames=fieldnames) так тоже можно

    writer.writeheader()

    for user in users:
        writer.writerow(user)

with open('user.csv') as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)

# ini или conf - конфигурационные файлы (обычно в windows) никаких инструментов для записи в Python нет

# xml - Extended Markup Lnguage (устарел) (крос-язычный) (lxml - модуль для парсинга xml и html, быстро и нересурсоёмко)

# xps


# ====================


# Базы данных SQLite3/2 - база данных в одном файле (поумолчанию есть поддержка в Python)



