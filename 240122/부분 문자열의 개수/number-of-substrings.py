a = input()
b = input()

leng = len(a)
cnt =0

for i in range(leng-1):
    if b == a[i:i+2]:
        cnt+=1
print(cnt)