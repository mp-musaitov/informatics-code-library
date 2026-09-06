# Простое число

# Простое число имеет ровно два натуральных делителя: 1 и само число.
# Числа меньше 2 простыми НЕ являются.

# 1. Понятный вариант — проверить делители от 2 до n - 1
n = 17
is_prime = True

if n < 2:
    is_prime = False
else:
    for divisor in range(2, n):
        if n % divisor == 0:
            is_prime = False
            break

print(is_prime)  # True

# 2. Быстрый вариант — достаточно проверять до sqrt(n)
n = 91
is_prime = True

if n < 2:
    is_prime = False
else:
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            is_prime = False
            break

print(is_prime)  # False, потому что 91 = 7 * 13

# Почему достаточно корня:
# если n = a * b, то хотя бы один из множителей не больше sqrt(n).

# 3. Оформим проверку функцией
def is_prime_number(n):
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True

print(is_prime_number(2))   # True
print(is_prime_number(17))  # True
print(is_prime_number(21))  # False

# 4. Вывести все простые числа на отрезке
for number in range(2, 51):
    if is_prime_number(number):
        print(number)

# 5. Посчитать простые числа в списке
numbers = [2, 4, 5, 8, 11, 15, 17]
count = 0
for number in numbers:
    if is_prime_number(number):
        count += 1
print(count)  # 4

# 6. Найти первое простое число не меньше заданного
n = 100
while not is_prime_number(n):
    n += 1
print(n)  # 101

# Частые ошибки:
# 1. Считать 1 простым числом. Это неверно.
# 2. Забыть обработать 0 и отрицательные числа.
# 3. После найденного делителя продолжать цикл, хотя можно сделать break.
# 4. Проверять делители до n, когда для одного большого числа достаточно sqrt(n).

# Универсальная функция:
# def is_prime_number(n):
#     if n < 2:
#         return False
#     for divisor in range(2, int(n ** 0.5) + 1):
#         if n % divisor == 0:
#             return False
#     return True
