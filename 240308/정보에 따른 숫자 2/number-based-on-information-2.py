from sys import stdin


def count_nearest_type(T, a, b):
    S = []
    N = []

    for _ in range(T):
        word, idx = stdin.readline().split()
        if word == "S":
            S.append(int(idx))
        elif word == "N":
            N.append(int(idx))

    S.sort()
    N.sort()
    s_idx, n_idx, cnt = 0, 0, 0

    for i in range(a, b + 1):
        while s_idx < len(S) - 1 and abs(i - S[s_idx]) > abs(i - S[s_idx + 1]):
            s_idx += 1
        ds = abs(i - S[s_idx])

        while n_idx < len(N) - 1 and abs(i - N[n_idx]) > abs(i - N[n_idx + 1]):
            n_idx += 1
        dn = abs(i - N[n_idx])

        if ds <= dn:
            cnt += 1

    return cnt


T, a, b = list(map(int, stdin.readline().split()))
print(count_nearest_type(T, a, b))