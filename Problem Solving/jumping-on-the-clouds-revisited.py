
# n = 10
# c = [1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0, 0]
# k = 3
# 97

# def jumpingOnClouds(c, k):
# c = c + [c[0]]
# print(c)


# c = [1, 0, 1, 0, 0, 1, 1, 0]
# k = 2
# health = 100
# for i in range(0+k, len(c), k):
#     print(c[i], end=' ')
#     if c[i] == 0:
#         health -= 1
#     if c[i] == 1:
#         health -= (1+2)
# print()
# print(health)


# print(jumpingOnClouds(c,k))




c = [1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0, 0]  # 1
# 0, 0, 0
k = 3
# c = [0, 0, 1, 0, 0, 1, 1, 0]
# k = 2
def jumpingOnClouds(c, k):
    health = 100
    i = k
    while True:
        print(f'index: {i}')
        if i >= len(c):
            # i += k
            print(f'i sisa = {i}')
            # i = k - ( abs((len(c) - i)) +1 )
            i -= len(c)
            print(f'i baru = {i}')
            # break

        # print(c[i], end=' ')
        if c[i] == 0:
            health -= 1
            print("health:", health)

        if c[i] == 1:
            health -= (1+2)
            print("health:", health)
        if i == 0:
            break
        i += k

        # return health
        # print("Final health:", health)
    return health



print(jumpingOnClouds(c, k))