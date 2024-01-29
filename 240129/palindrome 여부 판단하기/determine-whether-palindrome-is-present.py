A = input()
def palindrome(str_):
    str_R = str_[::-1]
    if str_ == str_R:
        print('Yes')
    else:
        print('No')

palindrome(A)