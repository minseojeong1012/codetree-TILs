n = int(input())

def calc(n):
    if n ==1 :
        return 1
    return calc(n-1)+n

print(calc(n))