 
lst = [1,2,3]
lst2 = lst
lst[2] = 1

#Словарь

d = {
	(1,2,3): 123
}



type #узнать тип пременной

#Пример
a = 3
type(a)

type(lst)


1 + '5' #целое число + строка

#вывод ошибка
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''

#Приведение переменной

int('5')
5

float('5')
5.0

str([1,2,3])
'[1,3,4]'

#привести кортеж к списку

list((1,2,3))
[1,2,3]

int(5.5)
5

int(5.9)
5

s = '5'
s = int(s)
5

int('0110', 2) #строка должна быть в той системе исчесления к которой хотим привести, тогда не будет ошибки
6

int('0112, 2')
'''
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0112, 2'
'''

#Операторы

#Арифметические + - * / % // - (целочисленное деление, остаток отбрасывается) ** - (возведение к степени)

#int(5 / 2) ровно 5 // 2 вывод 2

4 ** 0.5 #извлечение квадратного корня
2.0

#Сравнение == (ровно) != (не равно) <> (тоже не равно) > < >= <=

#Присваивание = += -= *= /= %= //= **=

a = 3
a = a + 2 или a += 2 #a будет равно 5

#логические and, or, not (еще оператор смены знака -)

#принадлежности in, not in (True или Fales)

#для проверки элемента в списке

10 in lst
True

#тождественности is, not is (True или Fales)

a = None
a is None
True

lst = [1,2,3]
lst2 = [1,2,3]
lst == lst2
True

lst is lst2
Fales

lst3 = lst
lst is lst3
True

#побитовые & (и) | (или) ^ (XOR) - (отрицание) << >> (сдвиг влево и вправо)

bool(6) ^ bool(5)
Fales

bool(6) ^ bool(0) (т.е 6 = True 0 = False поэтому True)
True

bool(6) ^ bool(None)
True

