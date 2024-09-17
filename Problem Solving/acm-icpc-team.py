# topic = ['10101', '11110', '00010']
topic = ['10101', '11100', '11010', '00101']


def cek(a, b):
    hasil = sum(x1 == '1' or x2 == '1' for x1, x2 in zip(a, b))
    return hasil

# BASE
# def cek_known(a, b):
#     counter = 0
#     for i in range(len(a)):
#         if int(a[i]) | int(b[i]) == 1:
#             counter += 1
#     return counter


# def acmTeam(topic):
#     hasil = []
#     for i in range(len(topic) - 1):
#         for j in range(i+1, len(topic)):
#             known_topic = cek_known(topic[i], topic[j])
#             hasil.append(known_topic)
#             print(f'({i+1, j+1}) --> {known_topic}')

#     print(f'hasil: {hasil}')
#     return [max(hasil), hasil.count(max(hasil))]


# ------------------------------------------------------------
# OPTIMIZED
def cek_known(a, b):
    return sum(c1 == '1' or c2 == '1' for c1, c2 in zip(a, b))


def acmTeam(topic):
    hasil = [cek_known(topic[i], topic[j]) for i in range(len(topic))
             for j in range(i+1, len(topic))]
    max_known = max(hasil)
    return [max_known, hasil.count(max_known)]


print(acmTeam(topic))
