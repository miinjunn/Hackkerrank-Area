def is_leap(year):
    leap = None
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    else:
        leap = False

    return leap


print(is_leap(2000))
print(is_leap(2400))
print(is_leap(2020))
print(is_leap(2024))
print(is_leap(1800))
print(is_leap(1900))
print(is_leap(2100))
print(is_leap(2200))
print(is_leap(2300))
print(is_leap(2500))
print(is_leap(1900))
