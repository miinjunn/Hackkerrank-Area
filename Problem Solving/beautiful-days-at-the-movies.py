i = 20
j = 23
k = 6


def beautifulDays(i, j, k):
    # Write your code here
    beautiful_day = []
    for i in range(i, j+1):
        balik = int(str(i)[::-1])
        beautiful_day.append(str(abs((i - balik)) / k))

    counter = 0
    for i in beautiful_day:
        if i[-1] == '0':
            counter += 1

    return counter

print(beautifulDays(i,j,k))