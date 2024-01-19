string = input()
leng = len(string)

if leng%2==0:
    for i in range(leng - 1, 0, -2):
        print(string[i], end = '')
else:
    for i in range(leng-2,0,-2):
        print(string[i], end ='')