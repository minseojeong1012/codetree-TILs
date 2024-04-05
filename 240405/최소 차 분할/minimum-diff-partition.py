from collections import deque

n = int(input())

numq = deque(list(map(int, input().split())))

q = deque()

num = numq.popleft()
q.append(num)
q.append(-num)

while numq:
    num = numq.popleft()
    num_set = set()
    while q:
        d = q.popleft()
        num_set.add(d + num)
        num_set.add(d - num)
    q = deque(num_set)

print(min(map(abs, q)))