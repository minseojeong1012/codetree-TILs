def f(lst, max_v):
    if len(lst) == 0:
        return max_v
    else:
        if max_v < lst[0]:
            return f(lst[1:], lst[0])
        else:
            return f(lst[1:], max_v)
        


a=int(input())
lst = list(map(int, input().split()))
a=f(lst[1:], lst[0])
print(a)