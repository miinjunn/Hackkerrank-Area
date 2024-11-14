# word = 'zaba'
word = 'abc'
h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5,
     5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]


def designerPdfViewer(h, word):
    word_ord = [ord(i) - 97 for i in word]
    h_result = [h[i] for i in word_ord]

    result = max(h_result) * len(h_result)
    return result


print(designerPdfViewer(h, word))