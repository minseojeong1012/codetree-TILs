n = int(input())
arr = list(map(int,input().split()))

arr.sort()
for i in arr:
    print(i, end = ' ')
print()
arr1 = list(reversed(arr))
for i in arr1:
    print(i, end = " ")