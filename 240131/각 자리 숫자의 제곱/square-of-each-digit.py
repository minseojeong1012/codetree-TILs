def num(n):
    if n <10:
        return n**2
    return num(n//10) +(n%10)**2

N = int(input())
print(num(N))