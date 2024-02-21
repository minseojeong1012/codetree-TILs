import sys

read = sys.stdin.readline
n = int(read().strip())
x, y= map(int, read().strip().split(" "))

for _ in range(1, n):
    a, b= map(int, read().strip().split(" "))
    
    #겹치지 않는경우
    if b< x or y<a:
        print("No")
        sys.exit(0)
    else:
        x = max(a, x)
        y = min(b, y)
print("Yes")