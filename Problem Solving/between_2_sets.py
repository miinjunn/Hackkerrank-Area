a = [2, 6]
b = [24, 36]


def getTotalX(a, b):
    for i in range(len(a)):
        a[i] = [i for i in range(a[i], min(b)+1, a[i])]

    for i in range(len(b)):
        b[i] = [j for j in range(1, b[i] + 1) if b[i] % j == 0]

    c = a + b

    # # alternatif buat sort nested list, based on key length (ASC)
    c.sort(key=lambda x: len(x))

    same_number = []
    for i in c[0]:
        is_common = True
        for j in c[1:]:
            if i not in j:
                is_common = False
                break
        if is_common:
            same_number.append(i)

    return len(same_number)


coba = getTotalX(a, b)
print(coba)
