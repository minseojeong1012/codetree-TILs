from sys import stdin
a = stdin.readline().strip()
b = stdin.readline().strip()

idx = 0
while idx <= len(a)-len(b):
    check = True
    for j in range(len(b)):
        if a[idx+j] != b[j]:
            check = False
            break
    # print(check, a[idx:idx+len(b)], b, idx)
    if check:
        a = a[:idx]+a[idx+len(b):]
        if idx != 0 and a[idx-1] == b[0]: #처음이 아니고 첫글자가 같으면 이전부터
            idx = idx-2 #idx-1부터 다시 보기 위함!
        else: #첫글자가 다른 경우와 처음인 경우
            idx = idx-1
    # print(a, idx)
    idx += 1
print(a)