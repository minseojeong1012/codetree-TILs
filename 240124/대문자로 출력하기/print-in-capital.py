s=input()


for i in s:
    if (i>="a" and i<="z") or (i>="A" and i <="Z"):
        print(i.upper(),end="")