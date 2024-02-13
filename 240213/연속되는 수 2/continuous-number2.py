n = int(input())
cnt = 0
result = 0
arr = []

for _ in range(n):
    a = int(input())
    arr.append(a)
    
for i in range(1, n):
    if arr[i] == arr[i-1]:
        cnt += 1
    
    else:
        result = max(cnt, result)
        cnt = 0
        
    result = max(cnt, result)

print(result+1)