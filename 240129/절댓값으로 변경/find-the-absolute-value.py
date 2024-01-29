n = int(input())
arr = list(map(int, input().split()))

def modify(arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = -arr[i]

modify(arr)
for elem in arr:
    print(elem, end=" ")