arr = input().split()

for i in range(0, len(arr), 1):
    arr[i] = int(arr[i])

min_val = arr[0]

for elem in arr:
    if elem <= min_val:
        min_val = elem

print(min_val)