class Info:
    def __init__(self, name, addr, area):
        self.name= name
        self.addr= addr
        self.area= area

n= int(input())
people= []
for _ in range(n):
    name, addr, area= tuple(input().split())
    people.append(Info(name, addr, area))

# 이름 받아오는 리스트 생성
arr= [person.name for person in people]
# sort 함수로 이름을 사전순으로 정렬
arr.sort()
# 이름 리스트의 가장 끝 이름과 같은 사람의 Info 출력
for i in range(n):
    if people[i].name == arr[n-1]:
        print(f"name {people[i].name}")
        print(f"addr {people[i].addr}")
        print(f"city {people[i].area}")