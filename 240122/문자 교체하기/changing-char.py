a,b= input().split()
arr = list(a)
arrr= list(b)
arrr[0], arrr[1] = arr[0], arr[1]

s = ''.join(arrr)
print(s)