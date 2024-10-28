# n = [12, 24, 10, 24]
# n = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# n = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]


# def breakingRecords(scores):
#     maxim = []
#     minim = []

#     for i in range(len(scores)):
#         if i == 0:
#             minim.append(scores[i])
#             maxim.append(scores[i])
#         elif scores[i] > scores[i-1]:
#             if max(maxim) > scores[i]:
#                 maxim.append(max(maxim))
#             else:
#                 maxim.append(scores[i])
#             minim.append(min(minim))
#         elif scores[i] < scores[i-1]:
#             if min(minim) > scores[i]:
#                 minim.append(scores[i])
#             else:
#                 minim.append(min(minim))
#             maxim.append(max(maxim))
#         elif scores[i] == scores[i-1]:
#             maxim.append(maxim[-1])
#             minim.append(minim[-1])
#     return [len(set(maxim))-1, len(set(minim))-1]


n = [10, 5, 20, 20, 4, 5, 2, 25, 1]


def breakingRecords(scores):
    if not scores:
        return [0, 0]

    max_score = scores[0]
    min_score = scores[0]
    max_breaks = 0
    min_breaks = 0

    for i in scores[1:]:
        if i > max_score:
            max_score = i
            max_breaks += 1
        elif i < min_score:
            min_score = i
            min_breaks += 1

    return [max_breaks, min_breaks]

# print(maxim)
# print(minim)

# print(len(set(maxim))-1)
# print(len(set(minim))-1)


coba = breakingRecords(n)
print(coba)
