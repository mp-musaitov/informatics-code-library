# ============================================================
# БЛОК 1. КОЛИЧЕСТВО СПОСОБОВ
# ============================================================

n = 6

ways = [0] * (n + 1)
ways[0] = 1

for position in range(1, n + 1):
    ways[position] = ways[position - 1]

    if position >= 2:
        ways[position] += ways[position - 2]

print(ways[n])


# ============================================================
# БЛОК 2. ЗАПРЕЩЁННЫЕ ПОЗИЦИИ
# ============================================================

n = 7
forbidden = {3, 6}

ways = [0] * (n + 1)
ways[0] = 1

for position in range(1, n + 1):
    if position in forbidden:
        continue

    ways[position] = ways[position - 1]

    if position >= 2:
        ways[position] += ways[position - 2]

print(ways[n])


# ============================================================
# БЛОК 3. МИНИМАЛЬНАЯ СТОИМОСТЬ
# ============================================================

cost = [0, 5, 2, 4, 1, 3]

dp = [0] * len(cost)
dp[1] = cost[1]

for position in range(2, len(cost)):
    dp[position] = cost[position] + min(
        dp[position - 1],
        dp[position - 2]
    )

print(dp[-1])


# ============================================================
# БЛОК 4. МАКСИМАЛЬНАЯ СУММА
# ============================================================

values = [0, 5, 2, 10, 1, 4]

dp = [0] * len(values)
dp[1] = values[1]

for position in range(2, len(values)):
    dp[position] = values[position] + max(
        dp[position - 1],
        dp[position - 2]
    )

print(dp[-1])


# ============================================================
# БЛОК 5. МИНИМАЛЬНОЕ КОЛИЧЕСТВО МОНЕТ
# ============================================================

coins = [1, 3, 4]
amount = 6

dp = [None] * (amount + 1)
dp[0] = 0

for current in range(1, amount + 1):
    for coin in coins:
        if current >= coin and dp[current - coin] is not None:
            new_count = dp[current - coin] + 1

            if dp[current] is None or new_count < dp[current]:
                dp[current] = new_count

print(dp[amount])


# ============================================================
# БЛОК 6. ВОССТАНОВЛЕНИЕ ВЫБРАННЫХ МОНЕТ
# ============================================================

dp = [None] * (amount + 1)
previous_coin = [None] * (amount + 1)

dp[0] = 0

for current in range(1, amount + 1):
    for coin in coins:
        if current >= coin and dp[current - coin] is not None:
            new_count = dp[current - coin] + 1

            if dp[current] is None or new_count < dp[current]:
                dp[current] = new_count
                previous_coin[current] = coin

selected = []
current = amount

while current > 0:
    coin = previous_coin[current]
    selected.append(coin)
    current -= coin

print(selected)


# ============================================================
# БЛОК 7. МОЖНО ЛИ НАБРАТЬ СУММУ
# ============================================================

numbers = [3, 5, 7, 9]
target = 12

possible = [False] * (target + 1)
possible[0] = True

for number in numbers:
    for current in range(target, number - 1, -1):
        if possible[current - number]:
            possible[current] = True

print(possible[target])


# ============================================================
# БЛОК 8. ДАННЫЕ ИЗ ФАЙЛА
# ============================================================

# Формат файла data.txt:
# первая строка — конечная позиция;
# вторая строка — запрещённые позиции.
#
# with open('data.txt') as f:
#     n = int(f.readline())
#     forbidden = set(map(int, f.readline().split()))
#
# ways = [0] * (n + 1)
# ways[0] = 1
#
# for position in range(1, n + 1):
#     if position in forbidden:
#         continue
#
#     ways[position] = ways[position - 1]
#
#     if position >= 2:
#         ways[position] += ways[position - 2]
#
# print(ways[n])
