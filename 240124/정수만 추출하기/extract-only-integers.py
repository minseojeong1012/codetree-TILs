a,b = input().split()
fila=''
filb=''
sum =0
for i in a:
    if i.isdigit():
        fila+=i
    else:
        break
for i in b:
    if i.isdigit():
        filb+=i
    else:
        break

print(int(fila)+int(filb))