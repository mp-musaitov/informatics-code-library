# НОД и НОК

# НОД — наибольший общий делитель двух чисел.
# НОК — наименьшее общее кратное двух чисел.

# 1. Готовая функция gcd() из модуля math
from math import gcd

a = 48
b = 18
print(gcd(a, b))  # 6

# 2. НОК через НОД
a = 12
b = 18
lcm = abs(a * b) // gcd(a, b)
print(lcm)  # 36

# Для ненулевых натуральных чисел можно писать и так:
# lcm = a * b // gcd(a, b)

# 3. В Python есть готовая функция lcm()
from math import lcm

print(lcm(12, 18))  # 36

# 4. Алгоритм Евклида вручную
a = 48
b = 18

while b != 0:
    a, b = b, a % b

print(a)  # 6

# Что происходит:
# 48, 18
# 18, 12
# 12, 6
# 6, 0
# Когда второй элемент стал 0, первый и есть НОД.

# 5. Своя функция НОД
def my_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(my_gcd(48, 18))  # 6

# 6. НОД нескольких чисел
numbers = [24, 36, 60]
result = numbers[0]
for number in numbers[1:]:
    result = gcd(result, number)
print(result)  # 12

# 7. НОК нескольких чисел
numbers = [4, 6, 10]
result = 1
for number in numbers:
    result = lcm(result, number)
print(result)  # 60

# 8. Проверка взаимной простоты
# Два числа взаимно просты, если их НОД равен 1.
a = 14
b = 25
if gcd(a, b) == 1:
    print('Взаимно простые')

# Частые ошибки:
# 1. Путать НОД и НОК.
# 2. В формуле НОК использовать обычное деление / вместо целочисленного //.
# 3. Пытаться писать gcd() без импорта from math import gcd.
# 4. Забыть, что gcd(0, 0) = 0, а формула НОК через деление требует аккуратности с нулями.

# Универсальные шаблоны:
# from math import gcd, lcm
# print(gcd(a, b))
# print(lcm(a, b))
#
# Алгоритм Евклида:
# while b != 0:
#     a, b = b, a % b
# print(a)
