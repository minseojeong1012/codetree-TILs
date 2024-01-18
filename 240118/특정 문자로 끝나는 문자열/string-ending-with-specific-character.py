arr=[]

for _ in range(10):
    arr.append(input())

code= input()

for i in range(10):
    if arr[i][-1] == code:
        print(arr[i])