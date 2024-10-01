# def cutTheSticks(arr):
#     # Write your code here


arr = [5, 4, 4, 2, 2, 8]


def cutTheSticks(arr):
    arr_set = {}
    for i in arr:
        arr_set.update({i: arr.count(i)})

    # print(arr_set)
    # print(min(arr_set))
    # print(sum(arr_set.values()))

    result = [sum(arr_set.values())]
    hapus = min(arr_set)
    while hapus in arr_set:
        arr_set.pop(hapus)
        if len(arr_set) == 0:
            break
        else:
            result.append(sum(arr_set.values()))
        hapus = min(arr_set)
    
    return result

print(cutTheSticks(arr))