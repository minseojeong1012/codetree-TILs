string = input()

a = dict()
for s in string:
    if s not in a:
        a[s] = 1
    else:
        a[s] += 1
ans = 0
for key in a.keys():
    if a[key] == 1:
        ans = key
        break

if ans == 0:
    print("None")
else:
    print(ans)