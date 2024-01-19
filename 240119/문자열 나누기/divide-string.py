n= int(input())
arr=list(input().split())
all=' '
cnt=0
for i in range(n):
    all+=arr[i]
len= len(all)
for i in range(1,len):
    print(all[i], end ='')
    cnt+=1
    if cnt%5==0:
        print()