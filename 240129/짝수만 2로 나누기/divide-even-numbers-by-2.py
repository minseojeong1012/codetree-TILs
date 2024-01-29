# 함수1 - 값 변환 x
# def func(arr):
#     for num in arr:
#         if num % 2 == 0:
#             num //= 2

# 함수2 - 매개변수 N
#def func(arr, N):
#   for i in range(N):
#        if arr[i] % 2 == 0:
#            arr[i] //= 2

# 함수3
def func(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2


n = int(input())
_list = list(map(int, input().split()))
func(_list)

for elem in _list:
    print(elem, end=' ')