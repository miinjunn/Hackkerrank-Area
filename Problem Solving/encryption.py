import math

# s = 'if man was meant to stay on the ground god would have given us roots'
s = 'feedthedog'
# s = 'haveaniceday'
# s = 'chillout'
# s = 'roqfqeylxuyxjfyqterizzkhgvngapvudnztsxeprfp'


def encryption_base(s):
    s = s.replace(' ', '')

    print(s)
    print(len(s))
    # squareroot
    l = len(s)
    sqroot = l ** (0.5)
    rows = math.floor(sqroot)
    columns = math.ceil(sqroot)

    counter = l
    while counter < rows * columns:
        s += '@'
        counter += 1

    print(sqroot)
    print(rows)
    print(columns)

    #
    if rows * columns < l:
        rows = columns
        counter = l
        while counter < rows * columns:
            s += '@'
            counter += 1

    print('-'*50)
    print(rows)
    print(columns)

    hasil = []
    transpose = ''
    for i in range(columns):
        for j in range(i, len(s), columns):
            transpose += s[j]

    print(s)
    print(transpose)
    for i in range(0, len(transpose), rows):
        temp = transpose[i:i+rows].rstrip('@')
        # if '@' in temp:
        #     temp = temp.rstrip('@')
        hasil.append(temp)
        # print(hasil)
    return hasil

# ----------------------------------------------------------------------


def encryption(s):
    s = s.replace(' ', '')
    l = len(s)
    sqroot = l ** (0.5)
    rows = math.floor(sqroot)
    columns = math.ceil(sqroot)

    counter = l
    while counter < rows * columns:
        s += '@'
        counter += 1

    if rows * columns < l:
        rows = columns
        counter = l
        while counter < rows * columns:
            s += '@'
            counter += 1

    hasil = []
    transpose = ''
    for i in range(columns):
        for j in range(i, len(s), columns):
            transpose += s[j]

    for i in range(0, len(transpose), rows):
        temp = transpose[i:i+rows].rstrip('@')
        hasil.append(temp)
    # return ' '.join(hasil)
    return hasil


# print(encryption_base(s))
print(encryption(s))

# f e e d
# t h e d
# o g


# f t o
# e h g
# e e
# d d

# fto ehg eed d

# c h i
# l l o
# u t

# cluhltio

# ----------------------------------------------------------------------
# OPTIMIZED VERSION
def encryption_optimized(s):
    s = s.replace(' ', '')
    l = len(s)
    rows = math.floor(l ** 0.5)
    columns = math.ceil(l ** 0.5)

    hasil = []

    for i in range(columns):
        temp = s[i::columns]
        hasil.append(temp)

    return hasil


print(encryption_optimized(s))
