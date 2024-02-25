n = int(input())

lines = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    lines.append((x1, x2))

inter_lines = {}

for line in lines:
    for i in range(line[0], line[1]):
        if i in inter_lines:
            inter_lines[i] += 1
        else:
            inter_lines[i] = 1
        

print(max(inter_lines.values()))