# -------------------------------------------------
# N 개의 수를 Priority Queue로 관리하기 - O(M log N)
# -------------------------------------------------
import heapq

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums = [-num for num in nums]
heapq.heapify(nums)


for _ in range(m):
    # 가장 큰 원소 찾고, 삭제까지 수행하기- O(log N)
    max_value = -heapq.heappop(nums)
    
    # 1 줄인 값 추가하기 - O(log N)
    heapq.heappush(nums, -(max_value - 1))

print(-nums[0])  # O(1)