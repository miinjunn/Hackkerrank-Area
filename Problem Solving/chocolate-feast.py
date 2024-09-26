# def chocolateFeast(n, c, m):
#     temp = n // c
#     total = temp
#     print(f'total awal: {total}')

#     while (n//c) >= m:
#         if temp % m:
#             total += temp//m
#             temp = (temp % m) + (temp // m)
#         elif temp % m == 0:
#             total += 1
#             break

#     return total


def chocolateFeast(n, c, m):
    total = n // c
    temp = total
    print(f'total awal: {total}')

    while temp >= m:
        counter = temp // m
        total += counter
        temp = (temp % m) + (counter)
    return total


# n = 16809
# c = 123
# m = 11668

# n = 15
# c = 3
# m = 2

# n = 10
# c = 2
# m = 5

# n = 12
# c = 4
# m = 4

n = 6
c = 2
m = 2

print(chocolateFeast(n, c, m))
