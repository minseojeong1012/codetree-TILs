n = int(input())
arr=[]
cnt=0
len_all = 0
for _ in range(n):
    arr.append(input())

abc= input()

for i in range(n):
    
    if arr[i][0] == abc:
        cnt+=1
        len_all+=len(arr[i])

avg = round(len_all/cnt, 2)
#avg= (len_all/n)
print(f'{cnt} {avg:.2f}')