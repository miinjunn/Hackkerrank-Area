n = 4


def viralAdvertising(n):
    shared = []
    liked = []
    cumulative = []
    for i in range(n):
        if i == 0:
            shared.append(5)
            liked.append(shared[i] // 2)
            cumulative.append(2)
        else:
            shared.append(liked[i-1] * 3)
            liked.append(shared[i] // 2)
            cumulative.append(liked[i] + cumulative[i-1])

    print(f'shared: {shared}')
    print(f'liked: {liked}')
    print(f'cumulative: {cumulative}')

    return cumulative[-1]


print(viralAdvertising(n))