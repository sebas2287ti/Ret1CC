def is_palindromo(word):
    a = 0
    b = len(word) - 1
    while a < b:
        if word[a] != word[b]:
            return False
        a += 1
        b -= 1
    return True


def convert_palindromo(word):
    n = len(word)
    if n == 0:
        return 0, ""
        
    dp = [[0] * n for _ in range(n)]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            if word[i] == word[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    
    min_ops = dp[0][n-1]

    izq = []
    der = []
    i, j = 0, n - 1
    
    while i <= j:
        if i == j:
            izq.append(word[i])
            i += 1
        elif word[i] == word[j]:
            izq.append(word[i])
            der.append(word[j])
            i += 1
            j -= 1  
        elif dp[i+1][j] < dp[i][j-1]:
            izq.append(word[i])
            der.append(word[i])
            i += 1
        else:
            izq.append(word[j])
            der.append(word[j])
            j -= 1 

    res = "".join(izq) + "".join(reversed(der))
    return min_ops, res
