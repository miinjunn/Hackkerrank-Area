k = 2
security_val = [3, 5, -2, -4, 9, 16]
# security_val = [2, -3, 4, 6, 1]


def gainMaxValue(security_val, k):
    total = []
    for i in range(len(security_val)):
        temp = []
        for j in range(i, len(security_val), k):
            temp.append(security_val[j])
        total.append(sum(temp))
    return max(total)


result = gainMaxValue(security_val, k)
print(result)
