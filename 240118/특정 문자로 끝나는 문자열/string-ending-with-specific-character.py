arr=[]
cnt=0

for _ in range(10):
    arr.append(input())

code= input()

for i in range(10):
    if arr[i][-1] == code:
        print(arr[i])
        cnt+=1
if cnt ==0:
    print("None")