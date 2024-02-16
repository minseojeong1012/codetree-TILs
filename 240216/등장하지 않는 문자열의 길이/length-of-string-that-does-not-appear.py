from sys import stdin
n = int(stdin.readline())
sentence = stdin.readline().strip()

def check(sentence, i): #i길이에 대해서 체크
    n = len(sentence)
    for j in range(n-i): #시작할 위치
        tmp = sentence[j:j+i+1]
        for k in range(j+i+1, n-i+1):
            # print(i, j, tmp, sentence[k:k+i+1])
            if tmp == sentence[k:k+i+1]:
                return True
    return False


ans = 0
for i in range(n): #현재 위치부터 이후에 체크할 길이
    if not check(sentence, i):
        ans = i+1
        break
print(ans)