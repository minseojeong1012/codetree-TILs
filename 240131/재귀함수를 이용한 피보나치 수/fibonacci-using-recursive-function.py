n = int(input())

def recur(n):
    if n==1:
        return 1
    if n==2:
        return 2

    return recur(n-1)+recur(n-2)

print(recur(n))