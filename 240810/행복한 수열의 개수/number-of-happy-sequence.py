def check_happy(sequence, m):
    count = 1
    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i-1]:
            count += 1
            if count >= m:
                return True
        else:
            count = 1
    return False

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

happy_count = 0

# Check rows
for row in grid:
    if check_happy(row, m):
        happy_count += 1

# Check columns
for col in zip(*grid):
    if check_happy(col, m):
        happy_count += 1

print(happy_count)