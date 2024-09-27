def pageCount(n, p):
    if n % 2 == 0:
        n += 1

    if p % 2 != 0:
        p = [p-1, p]
    else:
        p = [p, p+1]

    arr = [i for i in range(n+1)]
    d = []
    for i in range(0, n+1, 2):
        d.append(arr[i:i+2])

    print(d)
    print(p)

    awal = d.index(p)
    akhir = (len(d)-1) - d.index(p)
    total = [awal, akhir]
    print(total)
    return min(total)


print(pageCount(5, 4))
