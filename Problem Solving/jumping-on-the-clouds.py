# c = [0, 0, 1, 0, 0, 1, 0]
c = [0, 0, 0, 1, 0, 0]

# step = 0
# for i in range(len(c)):
#     if c[i+2] == 0:
#         step += 1
#         i += 2
#     else:
#         step += 1
#         i += 1


def jumpingOnClouds(c):
    step = 0
    pos = 0
    while pos+1 <= len(c)-1:
        if pos+2 <= len(c)-1 and c[pos+2] == 0:
            step += 1
            pos += 2
            print(f'pos: {pos}')

        else:
            step += 1
            pos += 1
            print(f'pos: {pos}')

    # print(step)
    return step


print(jumpingOnClouds(c))
