array = [0] * 100
n = int(input())
for _ in range(n):
    x1, x2 = map(int, input().split())
    for i in range(x1, x2+1):
        array[i-1] += 1
print(max(array))