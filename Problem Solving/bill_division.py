k = 1
bill = [3, 10, 2, 9]
b = 12

# 14/2 = 7 (anna's part)
# 12 is total money anna gives to bill
# 12 - 7 = 5 (anna's return)
# output = 5


def bonAppetit(bill, k, b):
    bill.pop(k)
    anna = sum(bill) // 2
    kembalian = b - anna
    if kembalian == 0:
        print('Bon Appetit')
    else:
        print(kembalian)

bonAppetit(bill, k, b)