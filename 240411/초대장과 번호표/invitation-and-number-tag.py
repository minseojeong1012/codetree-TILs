from sys import stdin
n, g = list(map(int, stdin.readline().split()))


people_groups = [[] for _ in range(n)] #각 사람이 속하는 그룹을 의미
groups = [set() for _ in range(g)]


for i in range(g):
    nums = list(map(int, stdin.readline().split()))[1:]
    for num in nums:
        num -= 1 #인덱스단위로 변환
        groups[i].add(num)
        people_groups[num].append(i)
# print(groups, people_groups)

visited = {0}
q = {0}

while q:
    key = list(q)[0]
    visited.add(key)
    q.remove(key)

    for g_num in people_groups[key]: #key가 포함된 그룹
        # print(g_num, key, people_groups[key])
        groups[g_num].remove(key)
        #삭제후 1명이면 초대장을 받음
        if len(groups[g_num]) == 1:
            p_num = list(groups[g_num])[0]
            if p_num not in visited:
                visited.add(p_num)
                q.add(p_num)
print(len(visited))