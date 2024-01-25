a_list = []
a_list = list(map(int, input().split()))

mini = float('inf')

for k in range(3):
    if mini > a_list[k]:
        mini = a_list[k]

#print(mini)
print(min(a_list))