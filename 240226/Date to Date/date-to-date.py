m1, d1, m2, d2 = map(int, input().split())

date= [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days = 1

for mon in range(m1, m2):
    days += date[mon - 1]

days -= d1
days += d2

print(days)