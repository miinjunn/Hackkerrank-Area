
# s = 'baab'
# s = 'aa'
# s = 'aaabccddd'
# s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'
# def superReducedString(s):
#     s += '0'
#     counter = ''
#     step = 0
#     while step < len(s)-1:
#         if s[step] == s[step+1]:
#             # print(f'step sekarang: {step}')
#             step += 2
#         else:
#             counter += s[step]
#             step += 1

#     return counter if len(counter) != 0 else "Empty String"


# print(superReducedString(s))

# -----------------------------------------------------------------------------------------------------------------------------
# s = 'baab'
# s = 'aa'
# s = 'aaabccddd'
# s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'

# def superReducedString(s):
#     s_set = {}
#     for i in s:
#         s_set.update({i: s.count(i)})
#     # print(s_set)
#     counter = ''
#     for ky, vl in s_set.items():
#         if vl % 2:
#             print(ky)
#             counter += ky
#     # print(counter)
#     return counter if len(counter) != 0 else "Empty String"
# print(superReducedString(s))

# -----------------------------------------------------------------------------------------------------------------------------
s = 'baab'
# s = 'aa'
s = 'aaabccddd'
# s = 'zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'


def superReducedString(s):
    s = [i for i in s]
    step = 0
    while step < len(s)-1:
        if step < 0:
            step = 0
        if s[step] == s[step+1]:
            s.pop(step)
            s.pop(step)
            step -= 1
        else:
            step += 1
        if len(s) == 1:
            break
    # print(''.join(s))
    return ''.join(s) if len(s) != 0 else "Empty String"



print(superReducedString(s))