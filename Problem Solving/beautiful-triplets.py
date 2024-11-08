# d = 3
# arr = [1, 2, 4, 5, 7, 8, 10]
d = 1
arr = [2, 2, 3, 4, 5]


# def beautifulTriplets(d, arr):
#     counter = 0
#     for i in range(len(arr)-2):
#         for j in range(i, len(arr)-1):
#             for k in range(j, len(arr)):
#                 if (arr[j] - arr[i]) == d and (arr[k] - arr[j]) == d:
#                     # print(arr[i], arr[j], arr[k])
#                     counter += 1
#     return counter


def beautifulTriplets(d, arr):
    arr_set = set(arr)
    counter = 0
    for i in arr:
        if i + d in arr_set and i + 2*d in arr_set:
            counter += 1
    return counter

print(beautifulTriplets(d, arr))
