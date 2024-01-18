s1 = input()
s2 = input()
s3 = input()

leng1, leng2, leng3 = len(s1), len(s2), len(s3)

if leng1 > leng2 and leng2 > leng3:
    print(leng1 - leng3)
elif leng1 > leng3 and leng3 > leng2:
    print(leng1 - leng2)
elif leng2 > leng1 and leng1 > leng3:
    print(leng2 - leng3)
elif leng2 > leng3 and leng3 > leng1:
    print(leng2 - leng1)
elif leng3 > leng1 and leng1 > leng2:
    print(leng3 - leng2)
elif leng3 > leng2 and leng2 > leng1:
    print(leng3 - leng1)
elif leng1==leng2 and leng2 > leng3:
    print(leng2-leng3)
elif leng1==leng2 and leng2 < leng3:
    print(leng3-leng2)
elif leng2==leng3 and leng1 > leng3:
    print(leng1-leng3)
elif leng2==leng3 and leng1 <leng3:
    print(leng3-leng1)
elif leng1==leng3 and leng2> leng3:
    print(leng2-leng3)
elif leng1== leng3 and leng2 < leng3:
    print(leng3-leng2)