NO_OF_CHARS = 256

def find_word_BM(text, word):
    m = len(word)
    n = len(text)

    badChars = badCharslist(word, m)

    i = 0
    while (i <= n - m):
        j = m - 1
        while j >= 0 and word[j] == text[i+j]:
            j -= 1

        if j < 0:
            print("La palabra se encuentra en el indice = {}".format(i))
            i += (m - badChars[ord(text[i+m])] if i+m < n else 1)
        else:
            i += max(1, j-badChars[ord(text[i+j])])


def badCharslist(word, size):
    badChars = [-1]*NO_OF_CHARS
    for x in range(size):
        badChars[ord(word[x])] = x
    return badChars