a = [7, 1, 3, 4, 1, 7]
# a = [1, 2, 3]


def minimumDistances(a):
    kelompok = {}
    for ky, vl in enumerate(a):
        if a.count(vl) > 1:
            # print(vl, ky)
            if vl not in kelompok:
                kelompok[vl] = [ky]
            elif vl in kelompok:
                kelompok[vl].append(ky)

    print(kelompok)
    if len(kelompok) > 0:
        for ky, vl in kelompok.items():
            kelompok[ky] = [abs(vl[1] - vl[0])]
        # result = min(kelompok, key=lambda x: kelompok[x])
        result = min(kelompok.values())
        print(kelompok)
        return result[0]
    else:
        return -1


print(minimumDistances(a))
