a = input()
b= input()
sum=0
fa=''
fb=''
for i in a:
    if i.isdigit():
        fa+=i
for i in b:
    if i.isdigit():
        fb+=i
print(int(fa)+int(fb))