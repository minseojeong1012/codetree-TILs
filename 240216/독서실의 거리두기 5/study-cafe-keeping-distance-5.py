from sys import stdin
n = int(stdin.readline())
base = stdin.readline().strip()

ans = 0
for i in range(n): #위치 선정
    if base[i] == '1': #사용자 있음
        continue
    tmp = float("inf")
    check = True
    for j in range(n):
        if check and (i == j or base[j] == '1'): #처음 1은 패스
            cnt = 1
            check = False
            continue
        elif check: #아직 1이 안나와서 패스
            continue
        if i == j or base[j] == '1': #이후에 1만나면 거리 계산
            # print(tmp)
            tmp = min(tmp, cnt)
            cnt = 1
        else:
            cnt += 1
    # print(i, j, tmp, cnt)
    ans = max(ans, tmp)
print(ans)