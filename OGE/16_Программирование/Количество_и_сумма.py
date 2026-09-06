# ОГЭ №16. Количество и сумма подходящих элементов

n = int(input())
count = 0
total = 0

for _ in range(n):
    x = int(input())

    # Замените условие на условие задачи.
    if x > 0:
        count += 1
        total += x

print(count)
print(total)

# Пример: программа считает количество положительных чисел
# и их сумму.
