s = input()
s = list(s)
leng = len(s)
target=s[1]
change=s[0]
for i in range(leng):
    if s[i] == target:
        s[i] = change
for i in s:
    print(i, end='')