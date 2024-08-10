n=int(input())
v=[False]*(n+1)
pick=[]


def get(cnt):
    if cnt==n:
        for elem in pick:
            print(elem,end=" ")
        print()

    for i in range(1,n+1):
        if v[i]:
            continue

        v[i]=True
        pick.append(i)

        get(cnt+1)

        v[i]=False
        pick.pop()


get(0)