# # a = [4, 6, 5, 3, 3, 1]
# # a.sort()
# # a = [1, 1, 2, 2, 4, 4, 5, 5, 5]

# # a_set = {}
# # for i in a:
# #     a_set.update({i: a.count(i)})
# # print(a_set)
# # # a_set_sorted = dict(sorted(a_set.items(), key=lambda x: x[1], reverse=True))
# # # print(a_set_sorted)


# # for ky,vl in a_set.items():
# #     if vl > 1:
# #         print(ky, vl)

a = [4,4,4,4, 6, 5, 3, 3, 2,2,2,1]

def pickingNumbers(a):
    a_set = {}
    for i in a:
        a_set.update({i: a.count(i)})
    print(a_set)

    akhir = 0
    for i in a_set:
        # ambil value dari key, misal key:4 maka valuenya ada 4 --->  4 ada 4
        l = a_set[i]
        # print(f'{i} --> {l}')

        # berdasarkan key, jika 4+1 ada pada dict
        if (i+1) in a_set:
            # maka l tadi akan nemampung value dari key 4 + 5 (4:4, 5:1),
            # jadi l = 4+1 = 5
            l += a_set[i+1]

        # print(f'l: {l}')
        # print(f'c: {akhir}')

        # lalu akhir menampung l (jika akhir masing kosong).
        # jika ada isinya, maka akhir membandingkan nilai dari akhir sebelumnya dengan l
        akhir=max(l,akhir)
        # print(f'max_c: {akhir}')
    return akhir


# ketika perulangan pertama, i=4, akhir kan masih kosong, maka:
# setelah perulangan pertama berakhir maka akhir = 5
# . . .
# pada i = 3 (3:2)
# l = 2, lalu key 4 ada pada list dengan value 4 (4 : 4)
# maka l = 2 + 4 = 6
# kemudian akhir membandingkan max dari akhir lama(5) dengan akhir baru(6)
# sehingga updated akhir = 6, fungsi return akhir = 6.
print(pickingNumbers(a))

