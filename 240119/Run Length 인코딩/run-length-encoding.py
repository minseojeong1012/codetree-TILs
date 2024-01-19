a = input()
res =''
current = a[0]
num = 1
for i in a[1:]:
    if i == current:
        num+=1
    else:
        res+=current
        res+=str(num)
        current =i
        num=1

res +=current
res+=str(num)
print(len(res))
print(res)