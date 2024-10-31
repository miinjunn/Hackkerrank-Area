s = 'saveChangesInTheEditor'


def camelcase(s):
    word = ''
    for i in s:
        if i.isupper():
            word += f'@{i}'
        else:
            word += i

    result = word.split('@')
    print(result)
    return len(result)


print(camelcase(s))
