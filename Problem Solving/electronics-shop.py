

b = 10
keyboards = [3, 1]
drives = [5, 2, 8]
# b = 5
# keyboards = [4]
# drives = [5]


def getMoneySpent(keyboards, drives, b):
    biaya = []
    for i in keyboards:
        for j in drives:
            if i + j <= b:
                biaya.append([i, j])

    # print(biaya)
    if len(biaya) == 0:
        return -1
    else:
        akhir = max(biaya, key=lambda x: sum(x))
        return sum(akhir)


print(getMoneySpent(keyboards, drives, b))