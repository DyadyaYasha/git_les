# Запускаемый файл 
#Импорт модуля целиком
import sys
# import sq_sh

# from sq_sh import * # * - импортировать всё (так делать нельзя)

# print(
#     sq_sh.calculate_square_area(4) # точка позволяет обращаться к функциям, переменным
# )

# какие есть имена в sq_sh

# print(dir(sq_sh))

# импорт модуля из пакета

import mega_math.sq_sh

# mega_math.sq_sh.calculate_square_area(5) # слишком громоздко

from mega_math import sq_sh # дальше работаем как и еслибы модуль лежал на одном уровне с исполняемым файлом

from mega_math.limit import do_something # импорт функции из модуля который лежит в пакете

from mega_math.sq_sh import * # так не делать



print(__name__) # если используется как запускаемый файл

if __name__ == '__main__':
    print(
        sq_sh.calculate_square_area(4) #если не будет этой команды, то если использовать этот файл как модуль будут исполняться все print'ы

    )

# print(sys.path) # (а также PYTHONPATH) переменная path - это список путей где python ищет модули


