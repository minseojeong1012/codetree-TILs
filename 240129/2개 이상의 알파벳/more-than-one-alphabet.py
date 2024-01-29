def f(a):
    for i in range(1, len(a)):
        if a[i] != a[0]:
            for i in range(len(a)):
                for j in range(i + 1, len(a)):
                    if a[i] == a[j]:
                        return True
    return False


a = input()
if f(a):
    print('Yes')
else:
    print('No')