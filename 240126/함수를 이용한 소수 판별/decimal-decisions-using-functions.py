def prime_number(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

a, b = tuple(map(int, input().split()))

sum_val = 0
for i in range(a, b+1):
    if prime_number(i):
        sum_val += i

print(sum_val)