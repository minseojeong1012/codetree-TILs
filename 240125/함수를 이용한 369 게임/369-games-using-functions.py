a,b = map(int,input().split())
def tfs(n,m):
    num = []
    for i in range(n,m+1):
        if '3' in str(i) or '6' in str(i) or '9' in str(i) or i%3==0:
            num.append(i)
    return len(num)
print(tfs(a,b))