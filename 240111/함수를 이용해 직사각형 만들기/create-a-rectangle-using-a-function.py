def show(a,b):
    for _ in range(a):
        print("1"*b)

a,b = map(int,input().split())
show(a,b)