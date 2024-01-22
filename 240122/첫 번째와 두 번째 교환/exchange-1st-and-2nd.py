s = input()
arr = list(s)
leng = len(s)
a = arr[0]
b = arr[1]

for i in range(leng):
    if arr[i] == a:
        arr[i] = b
    elif arr[i] == b:
        arr[i] = a

for i in arr:
    print(i, end ='')