# Строки в Python

Строка — последовательность символов.

```python
text = 'Python'
```

## Длина и индексы

```python
print(len(text))  # 6
print(text[0])    # P
print(text[-1])   # n
```

Индексация начинается с нуля. `-1` — последний символ.

## Срезы

```python
print(text[1:4])   # yth
print(text[:3])    # Pyt
print(text[3:])    # hon
print(text[::2])   # Pto
print(text[::-1])  # nohtyP
```

Правая граница среза не включается.

## Перебор строки

```python
for symbol in text:
    print(symbol)
```

По индексам:

```python
for i in range(len(text)):
    print(i, text[i])
```

## Поиск подстроки

```python
text = 'информатика'

if 'форма' in text:
    print('Подстрока найдена')

print(text.find('форма'))   # 2
print(text.find('python'))  # -1
```

## Основные методы

```python
text = '  Python для ЕГЭ  '

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace('Python', 'Питон'))
```

Строки неизменяемы: эти методы возвращают новую строку.

## count(), startswith(), endswith()

```python
text = 'абракадабра'
print(text.count('а'))  # 5

filename = 'result.txt'
print(filename.startswith('res'))
print(filename.endswith('.txt'))
```

## split() и join()

```python
text = '10 20 30 40'
parts = text.split()
```

Для получения чисел:

```python
numbers = list(map(int, input().split()))
```

Соединение строк:

```python
words = ['ЕГЭ', 'по', 'информатике']
text = ' '.join(words)
```

## Строку нельзя изменить по символу

```python
word = 'кот'
# word[0] = 'р'  # TypeError

word = 'р' + word[1:]
```

## Проверки символов

```python
symbol = '7'

print(symbol.isdigit())  # True
print(symbol.isalpha())  # False
```

## Частые ошибки

- начинать индексацию с 1;
- включать правую границу среза;
- пытаться изменить отдельный символ;
- забывать, что `split()` возвращает строки;
- ожидать, что строковые методы изменят исходную строку.

## Памятка

```python
len(text)
text[0]
text[-1]
text[a:b]
text[::-1]
text.count('a')
text.split()
```

Готовые примеры для быстрого копирования находятся в файле [`04_Строки.py`](04_Строки.py).

## Практика

[Практические задания по теме](PRACTICE.md) — разминка, основной и повышенный уровни, мини-задача в стиле ЕГЭ/ОГЭ.
