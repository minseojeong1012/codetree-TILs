s = input()
cnt=0
cntt=0
leng = len(s)

for i in range(leng-1):
    if 'ee' in s:
        cnt+=1
    elif 'eb' in s:
        cntt+=1

print(cnt,cntt)