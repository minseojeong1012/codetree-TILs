from sys import stdin #stdin함수를 가져오기 위한 코드
N, M = map(int, stdin.readline().split()) #A가 반복입력할 N횟수, B가 반복 입력할 M횟수 입력
pathA = [] #A가 각 횟수마다 입력한 방향과 이동거리를 원소별로 저장할 배열
pathB = []#B가 각 횟수마다 입력한 방향과 이동거리할 거리를 원소별로 저장할 배열
#아래부터 코드
for _ in range(N): #N번 반복시켜 
    d, t = stdin.readline().split()#A의 방향과 이동거리를 split()나눠 저장한다. 
    t = int(t)#t는 이동거리이므로 정수값으로 변환한다.
    pathA.append((d, t))#각 방향과 이동거리를 pathA에 하나의 원소로 저장 (각자따로 저장하면 오류가 뜸)

for _ in range(M):#M번 반복시켜
    d, t = stdin.readline().split()#B의 방향과 이동거리를 split()으로 저장
    t = int(t)#t는 이동거리이므로 정수로 변환
    pathB.append((d, t)) #각 방향과 이동거리를 하나의 원소로 pathB에 저장
#print(pathA) 각 배열 확인
#print(pathB)

#왜 함수를 썼나? pathA와 pathB에 대해 2가지를 계산해야함으로 함수 하나로 정의
def get_trace(path):#pathA, pathB를 인수로 받아
    cur = 0 #현 위치
    location = [] #pathA, pathB에 따라 변하는 cur값을 1초씩 저장
    for d, t in path: #방향과 이동거리를 받아
        if d =='L': #방향이 왼쪽일시
            for _ in range(t):# 이동거리크기만큼
                cur -= 1 #현재 위치값을 뺀다(왼쪽으로 이동)
                location.append(cur) #초마다 배열에 기록

        if d =='R':#방향이 오른쪽일시
            for _ in range(t):#이동크기만큼 반복
                cur += 1 #이동크기만큼 cur값을 증가시킴 (오른쪽 이동)
                location.append(cur) #초마다 배열에 현 위치를 기록
    return location #과정이 끝나면 초마다 기록된 배열을 돌려준다.

traceA = get_trace(pathA)#pathA를 인자로 넘긴다.
traceB = get_trace(pathB)#pathB를 인자로 넘겨 함수 계산
total_length = len(traceA) #가장 짧은 traceA를 길이로 잡는다.
ans = -1# 만약 서로 만나는 구간이 없을 시 ans 값을 출력하도록 -1을 저장
for i in range(total_length): #traceA의 길이를 기준으로 반복하여
    if traceA[i] == traceB[i]: #traceA의 요소와 traceB가 만날 시 
        ans = i + 1# ans에 만나는 인덱스와 -1에 대하여 +1을 더해준다.
        break #값을 찾을 시 if문을 탈출한다.
print(ans) #찾은 결과값을 출력한다.