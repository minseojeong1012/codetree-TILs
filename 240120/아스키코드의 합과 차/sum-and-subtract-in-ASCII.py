a,b = input().split()
aa = ord(a)
bb = ord(b)
c = aa+bb

if aa>bb:
    d = aa-bb
else:
    d = bb-aa

print(c, d)