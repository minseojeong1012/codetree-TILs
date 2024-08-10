from collections import deque 
n,t = map(int,input().split())
num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))
tot = num1 + num2 
tot = deque(tot)
count = 0 
while count < t :
    tot.appendleft(tot.pop())
    count+=1

while len(tot) > 0:
    for i in range(n):
        print(tot.popleft(),end=' ')
    print()