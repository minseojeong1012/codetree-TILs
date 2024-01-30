a = list(input())
b = list(input())
def bb(j,k):
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            print(i)
            break
    else:
        print(-1)
        

bb(a,b)