a, o, c = input().split()
a = int(a)
c = int(c)

def plus(n,m):
    return n+m

def minus(n,m):
    return n-m

def divv(n,m):
    return n//m

def multiple(n,m):
    return n*m


if o == "+":
    print(a, "+", c, "=", plus(a,c))
elif o == "-":
    print(a, "-", c, "=", minus(a, c))
elif o == "/":
    print(a, "/", c, "=", divide(a, c))
elif o == "*":
    print(a, "*", c, "=", multiple(a, c))
else:
    print("False")