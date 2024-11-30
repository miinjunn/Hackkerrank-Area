def repeatedString(s, n):
    sisa = n % len(s)
    # print(f'sisa : s[0:{sisa}]')
    if sisa == 0:
        sisa_s = 0
        a_pada_sisa_s = 0
    else:
        sisa_s = s[:sisa]
        a_pada_sisa_s = sisa_s.count('a')

    # print(f'sisa_s: {sisa_s}')
    # print(a_pada_sisa_s)
    total_a = s.count('a') * (n//len(s)) + a_pada_sisa_s
    return total_a


s1 = 'epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq'
n1 = 549382313570
# expected: 16481469408

s2 = 'aba'
n2 = 10
# expected: 7


print(repeatedString(s1, n1))
print(repeatedString(s2, n2))
