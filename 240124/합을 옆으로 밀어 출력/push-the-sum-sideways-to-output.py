n= int(input())
arr=[]
sum=0
for _ in range(n):
    arr.append(int(input()))

for i in arr:
    sum+=int(i)
sum = str(sum)
sum = sum[1:]+sum[0]
print(sum)