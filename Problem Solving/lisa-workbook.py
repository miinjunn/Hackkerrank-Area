n = 5
k = 3
arr = [4, 2, 6, 1, 10]


def workbook(n, k, arr):
    page = []
    for i in arr:
        temp = []
        for j in range(1, i+1):
            temp.append(j)
        page.append(temp)

    # print(page)
    chapter = []
    for i in page:
        # print(i)
        for j in range(0, len(i), k):
            chapter.append(i[j:j+k])

    print(chapter)
    # print(len(chapter))

    result = 0
    for i in range(len(chapter)):
        # print(f'{i+1} --> {chapter[i]}')
        if i+1 in chapter[i]:
            result += 1
            print(f'{i+1} --> {chapter[i]}')

    # print(result)
    return result


# workbook(n, k, arr)
print(workbook(n, k, arr))
