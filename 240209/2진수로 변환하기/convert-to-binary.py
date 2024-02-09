import sys

def get_binary(N):
    if N <= 1:
        return N
    return get_binary(N//2) * 10 + (N%2)

si = sys.stdin.readline

n = int(si())

print(get_binary(n))