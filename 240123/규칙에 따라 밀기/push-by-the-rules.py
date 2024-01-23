s = input()
op = input()


for elem in op:
    if elem == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)