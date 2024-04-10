# ---------------------------------------------
# N 개의 수를 배열로 관리하기 - O(N*M), 시간 초과
# ---------------------------------------------
n, m = map(int, input().split())
nums = list(map(int, input().split()))


def find_max_index(arr):
    """
    arr "배열"에서 가장 큰 원소가 존재하는 index를 return하는 함수이다. 시간 복잡도는 O(N)이다.
    """
    max_value, max_index = arr[0], 0
    for i in range(1, n):
        if max_value < arr[i]:
            max_value, max_index = arr[i], i
    
    return max_index


for _ in range(m):
    # 가장 큰 원소 찾기 - O(n)
    max_index = find_max_index(nums)
    
    # 해당 원소를 1 감소 시키기 - O(1)
    nums[max_index] -= 1

print(nums[find_max_index(nums)])