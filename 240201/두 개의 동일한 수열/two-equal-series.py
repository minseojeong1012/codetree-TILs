n=int(input())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
if set(arr1)==set(arr2):
    print('Yes')
else:
    print('No')