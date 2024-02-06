from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

result=[] #정렬하면서 들어감

def sort_in(elem):
    if len(result) == 0:
        result.append(elem)
        return
    for i in range(len(result)):
        if result[i] > elem: #앞이 작은 것 elem이 작으면 비교한 자리는 elem 자리가 됨
            result.insert(i, elem)
            return
    result.append(elem)
    return

for i in range(n):
    sort_in(arr[i])
    # print(result)
    if i%2==0: #홀수번째는 짝수인덱스 의미
        print(result[i//2], end=" ")