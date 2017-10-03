#функция

def hello():
   print('Hello, Function!')

#можно и так
# v = hello
# v()

#hello()

#аргументы функции

def hello(name):
    print('Hello,', name)

hello('Вася')
hello('Петя')

def login(user, password):
    print('Пользователь {} зашёл с паролем {}'.format(user, password))

#можно и так(но не рекомендуется)
# def login(user, password):
#     tamplate = 'Пользователь {} зашёл с паролем {}'
#     msg = template.format(user, password)
#     print(msg)

login('kyzima-spb', 1234567)
login('itmo-it', 6666)

# Изменяемые и не изменяемые типы данных

def parse(src, output):
    src = src.strip('.')

    for w in src.split():
        output.append(w)

src = 'Python is a programming language...'
lst = []

parse(src, lst)
print(src, lst)

# Аргументы со значением по умолчанию

def pow(x, p=2): #x - обязательный аргумент p=2 - не обязательный (опциональный) (он должен идти после обязательного!!)
    return x ** p #return возвращает значение (функция завершает свою работу(точно также как break в цикле))
# return x ** p, если поставить запятую то return будет возвращать кортеж
print(
    pow(2),
    pow(3, 8)
)

# def f(x, l=[]): # так делать нельзя!!!
def f(x, l=None):
    # l = [] if l is None else l длинно и некрасиво
    l = l or []
    print(l)
    l.append(x)

f(1)
f(2)
f(3)
f(4, [])

# Именованные аргументы

def func2(x, y):
    return x - y

print(
    func2(y=8, x=5), # к любому аргументу можно обратиться по имени (в любом порядке, если задано значение)
    func2(9, 6),
    func2(9, y=6)
) 

# Переменное количесво аргументов

def summa(*args): # *args - позицианнированные аргументы (кортеж (tuple)). **kwargs - именованные аргументы (словарь (dict))
# def summa(*args, *a): - не рекомендуется
# def summa(*args, start): - будет ошибка нужно так def summa(start, *args): тогда при вызове print(summa(1, 2, 3)) то start примет первый (1) аргумент а *args все остальные 
    return sum(args)

# дописать!!!!

# print(
#     summa(1, 2, 3)
#     summa(4, 10, 89, 78, 78)
#     summa(2, 2)
# )




login_data = ['user1', '1']
# login(login_data[0], login_data[1]) - так делать нельзя
login(*login_data) # количество аргументов в списке должно совпадать

login_data_dict = {
    'user': 'user2',
    'password': '2'
}

login(**login_data_dict) # в словаре должно быть только нужные нам значения

# Анонимная функция
# Как задать функцию без имени?

sqrt = lambda x : x ** 0.5 # return писать не нужно, lambda сама возвращает результат(быстрее и компактнее)

print(sqrt(9))

def func3(callback):
    callback()

func3(lambda : 'something') # в lambda можно передать несколько функций через запятую

# Замыкания

# Функция каррирования (частитчного применения)

def trim(chars=None):
    # замкнутая область видимости (живёт аргумент chars и все другие аргументы которые мы можем объявить, к этим аргументам может обращаться вложенная функция)
    def func(s):
        return s.strip(chars)
    return func

trim_spaces = trim()
trim_slashes = trim('/\\|')

# print(trim, trim_spaces, trim_slashes)

print(
    trim_spaces('    hello     \n'),
    trim_slashes('||||\\    hello\n////')
)


# Рекурсивная функция

def factorial(x):
    print(x)
    return 1 if x == 0 else x * factorial(x - 1)

print(factorial(5)) # (прямая рекурсия - внутри функции вызываем себяже)сжирает много памяти, если получится то рещать задачи без рекурсии

# Косвенная рекурсия

# def a():
#     b()

# def b():
#     a()  # бесконечная рекурсия


# область видемости и время жизни переменных

# Глобальные переменные
# все, кроме функций и классов

g = 666
lst = []
# Локальные переменные
# - тело функции
# - классы (поля классов)

def wrapper():
    # print('In function', g)
    # global g - даёт доступ к глобальной переменной
    # g = 777
    # print('In function', g)

    external = 777

    def func():
        global g # нужно когда мы хотим изменять переменные
        nonlocal external # нужно когда мы хотим изменять переменные
        # print(external) # читать может, но не редакировать
    lst.append(465)


wrapper()
print(g, lst)


