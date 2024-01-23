s = input()
leng = len(s)
print(s)
for i in range(leng):
    s = s[-1]+s[:-1]
    print(s)