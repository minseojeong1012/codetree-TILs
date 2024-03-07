"""
8:50~9:09
n개의 숫자.
출력: 임의의 숫자 두 개 사이에 자연수 k를 넣었을 때 등차수열에 되는 횟수의 최대.
입력----
1: n
2: n개의 숫자
"""
n=int(input())
arr=list(map(int, input().split()))
#k의 최대는 100
k_max=0
for k in range(1, 101):
    #두 수를 수열에서 뽑기
    cnt=0
    for i in range(n):
        for j in range(i+1, n): #####이부분을 i+1로 바꾸어야 맞았다고 뜹니다#####
            if (arr[i]+arr[j])/2==k:
                cnt+=1
    k_max=max(k_max, cnt)
print(k_max)