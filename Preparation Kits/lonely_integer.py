# a = [9, 1, 2, 3, 4, 3, 2, 1, 7, 8]
a = [84, 48, 13, 20, 61, 20, 33, 97, 34, 45, 6, 63, 71, 66, 24, 57, 92, 74, 6, 25, 51, 86, 48, 15, 64, 55, 77, 30, 56, 53, 37, 99, 9, 59, 57, 61, 30, 97, 50, 63, 59, 62, 39, 32, 34, 4, 96, 51, 8,
     86, 10, 62, 16, 55, 81, 88, 71, 25, 27, 78, 79, 88, 92, 50, 16, 8, 67, 82, 67, 37, 84, 3, 33, 4, 78, 98, 39, 64, 98, 94, 24, 82, 45, 3, 53, 74, 96, 9, 10, 94, 13, 79, 15, 27, 56, 66, 32, 81, 77]

# CARA - 1
# def lonelyinteger(a):
#     temp = {}
#     for i in a:
#         temp.update({i: a.count(i)})

#     result = min(temp, key=lambda x: temp[x])   # cara-1
#     # result = min(temp, key=temp.get)  # cara-2

#     return result

# -----------------------------------------------------------------


# CARA - 2


def lonelyinteger(a):
    oke = []
    for i in a:
        if a.count(i) == 1:
            oke.append([i, a.count(i)])
    return min(oke)[0]


print(lonelyinteger(a))
