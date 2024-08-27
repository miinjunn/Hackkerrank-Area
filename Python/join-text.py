import sys


def jointext(state_a, state_b):
    len_a = len(state_a)
    len_b = len(state_b)
    max_state = max(len_a, len_b)
    hasil = []
    for i in range(max_state):
        if i < len_a:
            hasil.append(state_a[i])
        if i < len_b:
            hasil.append(state_b[i])
    return ''.join(hasil)


input1 = sys.argv[1]
input2 = sys.argv[2]
output = jointext(input1, input2)
print(output, end="")
