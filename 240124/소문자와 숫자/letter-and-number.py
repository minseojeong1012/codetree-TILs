s = str(input())

for i in s :
    if i.isdigit() or (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z') :
        print(i.lower(), end = '')