def catAndMouse(x, y, z):
    mouseA = abs(x-z)
    mouseB = abs(y-z)
    if mouseA > mouseB:
        return 'Cat B'
    elif mouseA < mouseB:
        return 'Cat A'
    else:
        return 'Mouse C'


print(catAndMouse(1, 2, 3))
print(catAndMouse(1, 3, 2))
