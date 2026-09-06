# Делители числа

# Делитель числа n — число, на которое n делится без остатка.
# Главная проверка: n % divisor == 0.

# 1. Вывести все делители
n = 36
for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor)

# 2. Собрать делители в список
n = 36
divisors = []
for divisor in range(1, n + 1):
    if n % divisor == 0:
        divisors.append(divisor)
print(divisors)  # [1, 2, 3, 4, 6, 9, 12, 18, 36]

# 3. Посчитать количество делителей
n = 36
count = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        count += 1
print(count)  # 9

# 4. Сумма делителей
n = 12
total = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        total += divisor
print(total)  # 28

# 5. Собственные делители — без самого числа
n = 12
divisors = []
for divisor in range(1, n):
    if n % divisor == 0:
        divisors.append(divisor)
print(divisors)  # [1, 2, 3, 4, 6]

# 6. Поиск делителей до квадратного корня
# Делители образуют пары: для 36 это 1 и 36, 2 и 18, 3 и 12, 4 и 9, 6 и 6.
n = 36
divisors = []
for divisor in range(1, int(n ** 0.5) + 1):
    if n % divisor == 0:
        divisors.append(divisor)
        if divisor != n // divisor:
            divisors.append(n // divisor)
divisors.sort()
print(divisors)

# Этот вариант особенно полезен для больших чисел:
# вместо проверки всех чисел до n достаточно дойти примерно до sqrt(n).

# 7. Найти первый делитель больше 1
n = 91
first_divisor = None
for divisor in range(2, int(n ** 0.5) + 1):
    if n % divisor == 0:
        first_divisor = divisor
        break
print(first_divisor)  # 7

# 8. Найти числа на отрезке с заданным количеством делителей
for n in range(10, 31):
    count = 0
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            count += 1
    if count == 4:
        print(n)

# Частые ошибки:
# 1. Начинать range с 0 — делить на ноль нельзя.
# 2. Писать n % divisor вместо n % divisor == 0 в месте, где нужна явная проверка.
# 3. В range(1, n) забыть, что само n тогда не проверяется.
# 4. При поиске до корня дважды добавить sqrt(n), если n — полный квадрат.

# Универсальный шаблон:
# divisors = []
# for divisor in range(1, int(n ** 0.5) + 1):
#     if n % divisor == 0:
#         divisors.append(divisor)
#         if divisor != n // divisor:
#             divisors.append(n // divisor)
# divisors.sort()
