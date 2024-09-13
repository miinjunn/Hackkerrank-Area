from fractions import Fraction
from functools import reduce


def product(fracs):
    # t = # complete this line with a reduce statement
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator


fracs = []
for _ in range(int(input())):
    fracs.append(Fraction(*map(int, input().split())))
result = product(fracs)
print(*result)
