# n = 55
p = 1000
q = 10000
# p = 1
# q = 100


def cek_kep(n):
    d = len(str(n))
    pangkat = [i for i in str(n**2)]
    if len(pangkat) >= 2:
        awal = int(''.join(pangkat[:len(pangkat)-d]))
        akhir = int(''.join(pangkat[-d:]))
        res = awal + akhir
    elif len(pangkat) == 1:
        if pangkat[0] == '1':
            res = int(pangkat[0])
        else:
            res = None
    else:
        res = None
    return res


# print(cek_kep(9))


def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q+1):
        if i == cek_kep(i):
            result.append(i)
    if len(result) > 0:
        for i in result:
            print(i, end=' ')
    else:
        print('INVALID RANGE')


# # print()
kaprekarNumbers(p, q)
