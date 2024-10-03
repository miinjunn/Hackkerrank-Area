# height ?  --> 14


def utopianTree(n):
    tree = [0]
    period = n
    for i in range(period+1):
        if i % 2:
            tree.append(tree[i] * 2)
        else:
            tree.append(tree[i] + 1)
    tree.remove(0)
    return tree[n]


# n = [0, 1, 4]
n = 5


print(utopianTree(n))
