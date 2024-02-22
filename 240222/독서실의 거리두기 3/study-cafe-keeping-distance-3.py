n = int(input())
seat = list(map(int,input()))

def get_minDiff(arr):
    cnt = 0
    r = []
    for j in range(len(arr)):
        if arr[j] == 1:
            r.append(cnt)
            cnt = 0
        
        cnt += 1
    return min(r[1::])

ans = -1
for i in range(len(seat)):
    if seat[i] == 0:
        seat[i] = 1

        ans = max(get_minDiff(seat),ans)

        seat[i] = 0

print(ans)