from collections import Counter


customers = ['Bigcorp', 'Bigcorp', 'Acme', 'Bigcorp', 'Zork', 'Zork', 'Abc', 'Bigcorp', 'Acme', 'Bigcorp', 'Bigcorp',
             'Zork', 'Bigcorp', 'Zork', 'Zork', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'Bigcorp', 'Acme', 'LittleCorp', 'Nadircorp']

# print(len(customers))


def mostActive(customers):
    n = len(customers)
    statistik = Counter(customers)
    result = []
    for ky, vl in statistik.items():
        if vl/n >= 0.05:
            result.append(ky)

    result.sort()
    return result


print(mostActive(customers))
