# Функции в Python

Функция — именованный блок кода, который можно вызывать много раз.

## Простая функция

```python
def hello():
    print('Привет!')

hello()
```

## Параметры

```python
def greet(name):
    print('Привет,', name)

greet('Адам')
```

Несколько параметров:

```python
def add(a, b):
    print(a + b)
```

## return

```python
def multiply(a, b):
    return a * b

result = multiply(4, 6)
```

`print()` показывает значение, а `return` возвращает его из функции. Поэтому результат с `return` можно использовать дальше.

```python
answer = multiply(3, 5) + 10
```

## Функция-проверка

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

Часто можно короче:

```python
def is_positive(number):
    return number > 0
```

## return завершает функцию

```python
def check_number(number):
    if number < 0:
        return 'Отрицательное'
    if number == 0:
        return 'Ноль'
    return 'Положительное'
```

## Значение по умолчанию

```python
def greet_user(name='Гость'):
    print('Привет,', name)
```

## Именованные аргументы

```python
def student(name, score):
    print(name, score)

student(score=90, name='Адам')
```

## Локальные переменные

Переменная, созданная внутри функции, обычно доступна только внутри неё.

```python
def example():
    x = 10
    print(x)
```

## Вызов другой функции

```python
def square(number):
    return number ** 2

def sum_of_squares(a, b):
    return square(a) + square(b)
```

## Частые ошибки

- писать `hello` вместо `hello()`;
- путать `print()` и `return`;
- использовать локальную переменную вне функции;
- передавать неправильное количество аргументов;
- ожидать выполнения кода после `return`.

## Памятка

```python
def function_name(a, b):
    result = ...
    return result

def check(x):
    return условие
```

Готовые примеры для быстрого копирования находятся в файле [`06_Функции.py`](06_Функции.py).
