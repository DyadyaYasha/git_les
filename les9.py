# Исключения

class CustomError(Exception):
    pass

try:                    # в блоке try пишется код который потенциально приводит к ошибке
    n = int(input())
    import lalala
    raise TypeError('Что-то пошло не так') # выбрасывается исключение

except ValueError: # except можно типизировать т.е. написать какие ошибки отлавливать
    print('Не число!!')
except ImportError as e: # показывать описание ошибки
    print(e)

except (ImportError, TypeError) as a: # выводит кортеж
    print(a)

# в самом конце писать более общие ошибки