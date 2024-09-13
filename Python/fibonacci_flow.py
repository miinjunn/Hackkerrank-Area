def fib(n: int):
    if n == 0:
        return n
    if n == 1:
        return n
    return fib(n-1) + fib(n-2)


def bonacci(n: int):
    akhir = [0, 1]
    for i in range(2, n+1):
        akhir.append(akhir[i-1] + akhir[i-2])
    return akhir


angka = 10
print(fib(angka))
print(bonacci(angka))
