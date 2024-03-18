n = int(input())
arr = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr.sort()
arr2.sort()

for i in range(n):
    if arr[i] == arr2[i]:
        print("Yes")
        break
    else:
        print("No")