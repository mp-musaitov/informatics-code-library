# Функции в Python

# Функция — именованный блок кода, который можно вызывать много раз.

# 1. Простая функция
def hello():
    print('Привет!')

hello()
hello()

# 2. Параметры функции
def greet(name):
    print('Привет,', name)

greet('Магомед')
greet('Адам')

# 3. Несколько параметров
def add(a, b):
    print(a + b)

add(5, 7)  # 12

# 4. return — вернуть результат из функции
def multiply(a, b):
    return a * b

result = multiply(4, 6)
print(result)  # 24

# Важно: print() показывает значение на экране,
# а return возвращает его туда, откуда была вызвана функция.

# Поэтому результат функции с return можно использовать дальше:
answer = multiply(3, 5) + 10
print(answer)  # 25

# 5. Функция может содержать условия
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))  # True
print(is_even(7))  # False

# Такой код можно записать короче:
def is_positive(number):
    return number > 0

print(is_positive(10))  # True

# 6. return сразу завершает выполнение функции
def check_number(number):
    if number < 0:
        return 'Отрицательное'
    if number == 0:
        return 'Ноль'
    return 'Положительное'

print(check_number(-5))

# 7. Параметр со значением по умолчанию
def greet_user(name='Гость'):
    print('Привет,', name)

greet_user('Али')
greet_user()  # Привет, Гость

# 8. Именованные аргументы
def student(name, score):
    print(name, score)

student(score=90, name='Адам')

# 9. Локальные переменные
def example():
    x = 10
    print(x)

example()
# print(x)  # NameError: x существует только внутри функции

# 10. Глобальная и локальная переменные
x = 100

def show_x():
    x = 20
    print(x)  # 20 — локальная переменная

show_x()
print(x)      # 100 — глобальная переменная не изменилась

# 11. Функция для списка
def average(numbers):
    return sum(numbers) / len(numbers)

marks = [5, 4, 5, 3, 4]
print(average(marks))

# 12. Функция может вызывать другую функцию
def square(number):
    return number ** 2

def sum_of_squares(a, b):
    return square(a) + square(b)

print(sum_of_squares(3, 4))  # 25

# Частые ошибки
# 1. Забыть круглые скобки при вызове функции: hello вместо hello().
# 2. Перепутать print() и return.
# 3. Использовать локальную переменную за пределами функции.
# 4. Передать неправильное количество аргументов.
# 5. Написать код после return и ожидать, что он выполнится.

# Универсальные шаблоны

# Функция без параметров:
# def function_name():
#     действия

# Функция с параметрами:
# def function_name(a, b):
#     действия

# Функция, возвращающая значение:
# def function_name(a, b):
#     result = ...
#     return result

# Короткая функция-проверка:
# def check(x):
#     return условие
