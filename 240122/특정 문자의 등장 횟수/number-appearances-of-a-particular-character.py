s = input()
cnt=0
cntt=0
leng = len(s)

for i in range(leng-1):
    if 'ee' == s[i:i+2]:
        cnt+=1
    elif 'eb' ==s[i:i+2]:
        cntt+=1

print(cnt,cntt)