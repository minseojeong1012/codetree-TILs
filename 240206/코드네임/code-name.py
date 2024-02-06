codes = [
    tuple(input().split())
    for _ in range(5)
]

min = 0
for i in range(1, 5):
    code_name1, score1 = codes[min]
    code_name2, score2 = codes[i]
    if int(score1) > int(score2):
        min = i

code_name, score = codes[min]

print(f"{code_name} {int(score)}")