# n = 5  # prisoner
# m = 2  # candy
# s = 1  # start
# output: 2

# n = 5
# m = 2
# s = 2
# output: 3

# n = 7
# m = 19
# s = 2
# output: 6

# n = 3
# m = 7
# s = 3
# output: 3

n = 352926151
m = 380324688
s = 94730870
# 122129406


def saveThePrisoner(n, m, s):
    akhir = (m % n) + s-1
    if akhir > n:
        akhir = akhir - n
    if akhir == 0:
        akhir = n

    return akhir


print(saveThePrisoner(n, m, s))
# def saveThePrisoner(n, m, s):
#     if s != 1:
#         diff_s = s-1
#     else:
#         diff_s = 0
#     hasil = (m % n) + diff_s
#     return hasil
# print(saveThePrisoner(n, m, s))

# def saveThePrisoner(n, m, s):
#     if s != 1:
#         diff_s = s-1
#     else:
#         diff_s = 0

#     hasil = m % n + diff_s
#     if hasil > n:
#         hasil = hasil % n

#     return hasil


# print(saveThePrisoner(n, m, s))
# print(diff_s)
# ------------------------------------
# n = 352926151
# m = 380324688
# s = 94730870
# output = 122129406
# output = 122129406
# ------------------------------------


# output = 0
# while m != 0:
#     print(output)
#     output += 1
#     m -= 1

# akhir = output % n + (s-1)
# print('--------------')
# print(akhir)

# def saveThePrisoner(n, m, s):
#     return (m - 1 + s - 1) % n + 1

# ------------------------------------
# def saveThePrisoner(n, m, s):
#     temp = s
#     akhir = []
#     for i in range(s, m+s):
#         akhir.append(temp)
#         temp += 1
#         if temp == n+1:
#             temp = 1

#     return akhir[-1]


# print(saveThePrisoner(n,m,s))
