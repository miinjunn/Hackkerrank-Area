

# k = 3
# a = [-1, -3, 4, 2]
k = 2
a = [0, -1, 2, 1]


def angryProfessor(k, a):
    a.sort()
    # print(a)
    onTime = 0
    for i in a:
        if i <= 0:
            onTime += 1
        else:
            break

    # print(f'on time: {onTime}')
    if onTime >= k:
        return 'NO'
    else:
        return 'YES'


print(angryProfessor(k, a))
