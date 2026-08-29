def find_word_KMP(text, word): 
    n = len(text)
    m = len(word)

    lps = [0] * m
    res = []

    constructLps(word, lps)

    i = 0
    j = 0

    while i < n:
        if text[i] == word[j]:
            i += 1
            j += 1

            if j == m:
                res.append(i - j)
                j = lps[j - 1]
        
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return res 

def constructLps(word, lps):
    len_ = 0
    m = len(word)

    lps[0] = 0

    i = 1

    while i < m:
        if word[i] == word[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if lps[i] != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0 
                i += 1
    