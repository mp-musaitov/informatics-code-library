def fano(codes):
    for a in codes:
        for b in codes:
            if a != b and b.startswith(a):
                return False
    return True


codes = ['0', '10']
MAX_LENGTH = 5

best_sum = 10 ** 9
best_codes = None

for length1 in range(1, MAX_LENGTH + 1):
    for n1 in range(2 ** length1):
        code1 = bin(n1)[2:].zfill(length1)

        if code1 in codes:
            continue

        if not fano(codes + [code1]):
            continue

        for length2 in range(length1, MAX_LENGTH + 1):
            for n2 in range(2 ** length2):
                code2 = bin(n2)[2:].zfill(length2)

                if code2 in codes or code2 == code1:
                    continue

                if fano(codes + [code1, code2]):
                    total = sum(map(len, codes)) + length1 + length2

                    if total < best_sum:
                        best_sum = total
                        best_codes = [code1, code2]

print('Новые коды:', best_codes)
print('Минимальная суммарная длина:', best_sum)
