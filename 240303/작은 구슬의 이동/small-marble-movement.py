n, time=list(map(int, input().split()))
r, c, d=input().split()
r, c= int(r)-1, int(c)-1

dxs, dys = [0,1,-1,0],[1,0,0,-1]

direc={'U': 2, 'D':1, 'R':0, 'L':3}
direction=direc[d]
def in_range(r, c):
    return r>=0 and r<n and c>=0 and c<n

for t in range(time):
    nr= r+dxs[direction]
    nc= c+dys[direction]
    if in_range(nr, nc):
        r, c=nr, nc
    else:
        direction=3-direction

print(r+1, c+1)