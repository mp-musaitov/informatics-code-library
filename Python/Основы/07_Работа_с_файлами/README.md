# Работа с файлами в Python

В задачах по информатике данные часто находятся не в `input()`, а в текстовом файле.

## Открытие файла

```python
file = open('input.txt', 'r', encoding='utf-8')
text = file.read()
file.close()
```

Удобнее использовать `with`:

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read()
```

Файл закроется автоматически.

## Чтение строк

```python
line = file.readline()
lines = file.readlines()
```

Символ перевода строки `\n` часто убирают методом `strip()`.

## Перебор построчно

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        print(line)
```

## Числа в файле

Одно число в строке:

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)
```

Несколько чисел в строке:

```python
numbers = list(map(int, line.split()))
```

Все числа в список:

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    numbers = [int(line) for line in file]
```

## Первая строка — количество

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    numbers = []
    for _ in range(n):
        numbers.append(int(file.readline()))
```

## Запись

Режим `'w'` создаёт новый файл или очищает существующий:

```python
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write('Привет!')
```

Для записи числа:

```python
file.write(str(number))
```

Режим `'a'` добавляет данные в конец, не удаляя существующие.

## Типовой пример обработки

```python
count = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        number = int(line)

        if number % 2 == 0:
            count += 1

print(count)
```

## Частые ошибки

- неправильное имя или путь к файлу;
- забыть, что `readline()` возвращает строку;
- забыть `int()`;
- забыть `strip()`, когда мешает `\n`;
- открыть нужный файл в режиме `'w'` и стереть его;
- передать число напрямую в `write()`;
- не закрыть файл при обычном `open()`.

## Памятка

```python
with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        ...

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(str(result))
```

Готовые примеры для быстрого копирования находятся в файле [`07_Работа_с_файлами.py`](07_Работа_с_файлами.py).
