arr= list(input())
leng= len(arr)
for i in range(leng):
    if arr[i] == 'e':
        arr.pop(i)
        break
for i in arr:
    print(i, end='')