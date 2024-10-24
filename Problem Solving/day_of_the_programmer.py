# cek = [1984, 2000, 2400, 2020, 2024, 1800, 1900, 2100,
#        2200, 2300, 2500, 2023, 2016, 2017, 2012]
cek2 = [1984, 2017, 2016, 1800, 2100, 2200, 1918]

# normal leap


def leap(year: int):
    is_leap: int = None
    if year % 4 == 0:
        is_leap = 1
        if year % 100 == 0:
            is_leap = 0
            if year % 400 == 0:
                is_leap = 1
    else:
        is_leap = 0
    return is_leap


# normal leap
def G_leap(year: int):
    is_leap: int = None
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        is_leap = 1
    # elif year % 400 == 0 or year % 100 != 0:
        # is_leap = 1
    else:
        is_leap = 0
    return is_leap


def dayOfProgrammer(year):
    transisi: int = 1918
    if year > transisi:
        cek = leap(year)
        if cek == 1:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'
    elif year == transisi:
        return f'26.09.{year}'
    else:
        if year % 4 == 0:
            return f'12.09.{year}'
        else:
            return f'13.09.{year}'


for i in cek2:
    print(f'{i} : {G_leap(i)} --> {dayOfProgrammer(i)}')

# print(dayOfProgrammer(2017))
