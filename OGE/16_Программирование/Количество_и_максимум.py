# ОГЭ №16. Количество и максимум среди подходящих элементов

n = int(input())
count = 0
maximum = None

for _ in range(n):
    x = int(input())

    # Замените условие на условие задачи.
    if x % 3 == 0:
        count += 1

        if maximum is None or x > maximum:
            maximum = x

print(count)
print(maximum)

# None используется вместо начального нуля,
# потому что подходящие числа могут быть отрицательными.
