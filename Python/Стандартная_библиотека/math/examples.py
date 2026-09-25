# math: практическая шпаргалка
# Независимые блоки: копируйте нужный вместе с импортами и данными.

# БЛОК 1. НОД и НОК
from math import gcd, lcm

a, b = 18, 24
print(gcd(a, b))  # 6
print(lcm(a, b))  # 72

# БЛОК 2. Проверка полного квадрата
from math import isqrt

n = 144
if n >= 0:
    root = isqrt(n)
    print(root * root == n)  # True
else:
    print(False)

# БЛОК 3. Все делители положительного числа
from math import isqrt

n = 36  # n > 0
divisors = []
for d in range(1, isqrt(n) + 1):
    if n % d == 0:
        divisors.append(d)
        if d != n // d:
            divisors.append(n // d)
print(sorted(divisors))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]

# БЛОК 4. Округление вверх и вниз
from math import ceil, floor

print(ceil(2.3), floor(2.3))    # 3 2
print(ceil(-2.3), floor(-2.3))  # -2 -3
n, capacity = 101, 10
print((n + capacity - 1) // capacity)  # 11 упаковок

# БЛОК 5. Подсчёт без перебора
from math import factorial, comb

print(factorial(5))  # 120 порядков для пяти разных объектов
print(comb(5, 2))    # 10 пар без учёта порядка

# БЛОК 6. Корень и расстояние
from math import sqrt, hypot, pi

print(sqrt(49))  # 7.0
x1, y1 = 1, 2
x2, y2 = 4, 6
print(hypot(x2 - x1, y2 - y1))  # 5.0
radius = 2
print(round(pi * radius ** 2, 2))  # 12.57

# Частые ошибки
# 1. Перебирать делители только до isqrt(n), не включая сам корень.
# 2. Добавлять корень дважды в список делителей полного квадрата.
# 3. Использовать sqrt для точной проверки огромных целых.
# 4. Путать int(-2.7) и floor(-2.7): это -2 и -3.
# 5. Передавать отрицательные числа в sqrt, isqrt или factorial.
