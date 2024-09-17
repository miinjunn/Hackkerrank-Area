s = 'y'
t = 'yu'
k = 2
# s = 'hackerhappy'
# t = 'hackerrank'
# k = 9
# s = 'aba'
# t = 'aba'
# k = 7
# s = ['a', 's', 'h', 'l', 'e', 'y']
# t = ['a', 's', 'h']
# s = 'ashley'
# t = 'ash'
# k = 2


# s = 'zzzzz'
# t = 'zzzzzzz'
# k = 4
# same = []
# diff_s = ''
# diff_t = ''


def appendAndDelete(s, t, k):

    if len(t) < len(s):
        diff_s = 0
        diff_t = ''
        for i in range(len(t)):
            if t[i] == s[i]:
                # s.remove(s[i])
                # print(f'kata: {t[i]}')
                diff_s += 1
            else:
                diff_t += t[i:]
                break

        diff_s_word = s[diff_s:]
        # print(f'diff_s: {diff_s_word}')
        # print(f'diff_t: {diff_t}')

        result = k - (len(diff_s_word) + len(diff_t))
        # print(f'result -> {result}')

        if result >= 0:
            return 'Yes'
        else:
            return 'No'

    elif len(t) >= len(s):
        counter = 0
        for i in range(len(s)):
            if s[i] == t[i]:
                counter += 1
            else:
                break
        if k - (len(t[counter:]) + len(s[counter:])) >= 0:
            return 'YES'
        else:
            return 'NO'


print(appendAndDelete(s, t, k))


# for i in range(len(t)):
#     if t[i] == s[i]:
#         same.append(t[i])
#     else:
#         # print(diff.append())
#         diff_s += s[i:]
#         diff_t += t[i:]
#         break


# diff_angka_s = len(diff_s)
# diff_angka_t = len(diff_t)

# print(f'same: {same}')
# print(f'diff: {diff_s}')
# print(f'diff_angka_s: {diff_angka_s}')

# sisa_k = k - diff_angka_s
# print(f'sisa-k: {sisa_k}')

# sisa_k = sisa_k - diff_angka_t
# print(f'diff_angka_t: {diff_angka_t}')
# print(f'sisa-k: {sisa_k}')

# if sisa_k >= 0:
#     print('YES')
# else:
#     print('NO')

# if s == t:
#     print('Yes')
