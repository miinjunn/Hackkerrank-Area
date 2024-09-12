words = 'HackerRank.com presents "Pythonist 2".'


def swap_case(s):
    new = ''
    for i in s:
        if i.isupper() == True:
            new += i.lower()
        else:
            new += i.upper()

    return new


print(swap_case(words))
