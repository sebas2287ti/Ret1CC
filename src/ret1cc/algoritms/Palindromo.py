def is_palindromo(word):
    a = 0
    b = len(word) - 1
    while a < b:
        if word[a] != word[b]:
            return False
        a += 1
        b -= 1
    return True


def type_case_palindromo(word):
    return False

def case_one_palindromo(word):
    pass

def case_two_palindromo(word):
    pass
