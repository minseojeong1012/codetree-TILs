n = int(input())
arr = list(map(int,input().split()))

def insertion_sort():
    for i in range(1,n):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

insertion_sort()

for e in arr:
    print(e,end = " ")