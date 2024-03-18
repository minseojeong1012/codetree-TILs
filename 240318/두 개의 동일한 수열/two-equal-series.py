n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr.sort()
arr2.sort()
sum = 0
for i in range(n):
    if arr[i] == arr2[i]:
        sum +=1
    else:
        continue

if sum == n:
    print("Yes")
else:
    print("No")