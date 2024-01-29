def calc(x,y):
    a = min(x,y) + 10
    b = max(x,y) * 2
    return a,b

a,b = map(int,input().split())

x,y = calc(a,b)

print(x,y)