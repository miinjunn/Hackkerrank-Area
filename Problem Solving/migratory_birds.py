# arr = [1, 4, 4, 4, 5, 3]
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print(arr)


def migratoryBirds(arr):
    sarr = {}
    for i in range(1, 6):
        sarr.update({(i): arr.count(i)})

    # result = max(zip(sarr.values(), sarr.keys()))[1]   #cara-1
    # result = max(sarr, key=sarr.get)    #cara-2
    result = max(sarr, key=lambda x: sarr[x])  # cara-3
    return result


print(migratoryBirds(arr))
