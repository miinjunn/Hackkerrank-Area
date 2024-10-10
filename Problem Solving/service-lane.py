# def serviceLane(n, cases):
#     # Write your code here


n = 8
width = [2, 3, 1, 2, 3, 2, 3, 3]
cases = [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]


def serviceLane(n, cases):
    car = []
    for i in cases:
        car.append(min(width[i[0]:i[1]+1]))
        print(width[i[0]:i[1]+1])

    # print(car)
    return car

print(serviceLane(n, cases))