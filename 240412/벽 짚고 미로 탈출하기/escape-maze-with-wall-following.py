n = int(input())
x,y = map(int,input().split())
maps = [ list(input()) for _ in range(n)]

dxs=[0,1,0,-1]
dys=[1,0,-1,0]

#아래일때 체크해서 있으면 오른족 방향으로 진행
# 왼쪽일때 벽있으면 아래로 진행 벽없으면 방향 전환, 
# 위일때 벽있으면 왼쪽으로 진행 벽없으면 방향 전환
# 방향 바꾸는것과 탐색하는게 다르게 가야한다. 

# 인덱스 보정
x -= 1
y -= 1 

def in_range(x,y) : 
    return 0<= x < n and 0<= y < n 

def simulation() :
    global x,y
    global count
    pos = 0 # 초기는 오른쪽 
    wall = 1
    # while문 판단자 
    possible = True 
    # 이동카운트
    count = 0  
    # 방향바꿈 카운트
    pos_check = 0
    while possible : 
        # 벽짚기 
        if not in_range(x,y): # 반시계 방향 나온거 체크 
            #count += 1 
            return

        if count >= 10000 or pos_check >= 10000:
            count = -1
            break
        nx ,ny = x+dxs[wall], y + dys[wall] 

        checked = False
        # 오른짚기 벽체크
        if in_range(nx,ny):
            if maps[nx][ny] == '#' : # 벽이라면, 
                #바라보는 방향 벽체크 
                tx,ty = x+dxs[pos], y  + dys[pos] # 반시계 방향 체크를위해 
                if in_range(tx,ty) : 
                    if maps[tx][ty] == '#':#반시계방향회전 
                        pos = (pos+3) % 4 
                        wall = (wall +3) % 4
                        pos_check += 1 
                        checked = True

                if checked != True:
                    x,y = x + dxs[pos] , y + dys[pos] # 그냥 진행방향으로 가기. 
                    count += 1 
                else : 
                    pass
            elif maps[nx][ny] == '.' : # 길이라면 
                x,y = nx,ny #그쪽으로 진행 
                count +=1
                pos = (pos +1)%4
                wall =(wall+1)%4
                pos_check += 1 
        else : #바깥이다. 
            count += 1 # 밖으로 이동하며 끝 
            return
        
simulation()
print(count)