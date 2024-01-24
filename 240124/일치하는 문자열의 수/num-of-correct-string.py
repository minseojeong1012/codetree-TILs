n, a = input().split()
arr=[]
cnt=0
for _ in range(int(n)):
    arr.append(input())
for i in arr:
    if i==a:
        cnt+=1
print(cnt)