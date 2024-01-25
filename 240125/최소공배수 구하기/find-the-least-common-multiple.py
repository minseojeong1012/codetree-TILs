# 변수 선언 및 입력:
n, m = (map(int, input().split()))


# n과 m의 최대공약수를 반환합니다.
def find_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    return(gcd)
qq= find_gcd(n,m)
lcm = (n*m)//qq
print(lcm)