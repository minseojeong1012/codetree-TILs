n = int(input())
nums = list(map(int, input().split()))

nums.sort()
sum_max = 0

while nums:
    num1 = nums.pop(0)
    num2 = nums.pop(-1)

    num_sum = num1 + num2
    
    if num_sum > sum_max:
        sum_max = num_sum

print(sum_max)