a, b, c = tuple(map(int, input().split()))

def digit_sum(n):
    if n < 10:
        return n

    return digit_sum(n // 10) + n % 10


print(digit_sum(a * b * c))