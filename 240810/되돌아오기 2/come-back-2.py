n = list(map(str, input().strip()))
degree = 1
direction = 1

# 서 북 동 남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
x, y = 0, 0
ans = -1
count = 0

def move(direction):
    global x
    global y
    global count
    global ans
    x, y = x + dx[direction], y + dy[direction]
    if x == 0 and y == 0:
        ans = count
        return True
    return False
for i in n:
    count += 1
    if i == 'F':
        temp = move(direction)
        if temp:
            break

    elif i == 'L':
        direction = (direction + 3) % 4
    else:
        direction = (direction + 1) % 4
print(ans)