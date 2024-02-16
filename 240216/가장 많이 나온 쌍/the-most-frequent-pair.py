n,m=map(int,input().split())
array=[list(map(int,input().split())) for _ in range(m)]
answer=0

for i in range(m):
    temp=0
    for j in range(m):
        if array[i]==array[j] or array[i]==[array[j][1],array[j][0]]:
            temp+=1
    answer=max(answer,temp)
print(answer)