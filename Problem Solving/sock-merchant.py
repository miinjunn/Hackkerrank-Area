# m = {}
arr = [1, 2, 1, 2, 1, 3, 2]
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
arr.sort()
# n = set(arr)
# print(n)
print(arr)


def sockMerchant(n, ar):
    sendiri = 0
    pasangan = 0
    for i in set(ar):
        counter = 0
        if ar.count(i) > 1:
            counter = ar.count(i) // 2
            pasangan += counter
            if ar.count(i) % 2 != 0:
                sendiri += 1
        else:
            sendiri += 1
    return pasangan


# print(f'sendiri: {sendiri}')
# print(f'pasangan: {pasangan}')

print(sockMerchant(9, arr))
