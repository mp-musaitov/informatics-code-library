# ОГЭ №16. Количество и минимум среди подходящих элементов

n = int(input())
count = 0
minimum = None

for _ in range(n):
    x = int(input())

    # Замените условие на условие задачи.
    if x % 5 == 0:
        count += 1

        if minimum is None or x < minimum:
            minimum = x

print(count)
print(minimum)

# None позволяет корректно работать и с положительными,
# и с отрицательными значениями.
