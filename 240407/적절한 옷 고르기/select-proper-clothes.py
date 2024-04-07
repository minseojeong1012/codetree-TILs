MAX_COLOR = 1000

max_value = 0
n, m = map(int,input().split())
clothes_list = list(
    tuple(map(int,input().split())) for _ in range(n)
    )

memo = [
    [-1] * (MAX_COLOR + 1)
    for _ in range(m + 1)
]
#print(clothes_list)

def recursive(day, prev_color):
    if day == m + 1:
        return 0

    if memo[day][prev_color] != -1:
        return memo[day][prev_color]
    
    best_satisfaction = 0
    for cloth in clothes_list:
        #print(day, cloth)
        if cloth[0] <= day and cloth[1] >= day:
            best_satisfaction = max(best_satisfaction, 
                                    recursive(day + 1, cloth[2]) + abs(cloth[2] - prev_color))
    
    memo[day][prev_color] = best_satisfaction
    return memo[day][prev_color]


best_answer = 0
for cloth in clothes_list:
    if cloth[0] <= 1 and cloth[1] >= 1:
        best_answer = max(best_answer, recursive(2, cloth[2]))

print(best_answer)