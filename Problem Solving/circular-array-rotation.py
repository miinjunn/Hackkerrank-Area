# a = [3, 4, 5]
# k = 2
# queries = [1, 2]
a = [1, 2, 3]
k = 2
queries = [0, 1, 2]


def circularArrayRotation(a, k, queries):
    for _ in range(k):
        a.insert(0, a[-1])
        a.pop()

    # print(a)
    result = [a[i] for i in queries]
    return result


print(circularArrayRotation(a, k, queries))
