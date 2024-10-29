
x = 12
x = 1012


def findDigits(n):
    m = str(n)
    m = [int(i) for i in m]
    print(f'm: {m}')

    temp = []
    for i in m:
        if i == 0:
            continue
        if n % i == 0:
            temp.append(i)

    print(f'temp: {temp}')
    return len(temp)


print(findDigits(x))
