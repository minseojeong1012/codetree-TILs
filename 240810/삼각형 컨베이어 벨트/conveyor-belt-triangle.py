n,t = map(int,input().split())

one = list(map(int,input().split()))
two = list(map(int,input().split()))
three = list(map(int,input().split()))

for _ in range(t):

    # one의 맨뒤 제거후 two 앞에 넣기
    two.insert(0,one.pop())
    # two의 맨뒤 제거후 three앞에 넣기
    three.insert(0,two.pop())
    # three의 맨뒤 제거후 one 앞에 넣기
    one.insert(0,three.pop())

print(*one)
print(*two)
print(*three)