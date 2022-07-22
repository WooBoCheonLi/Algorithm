from math import sqrt
x, y, c = map(float, input().split())
start, end = 0, min(x, y)


def get_c(mid):
    a = sqrt(x**2-mid**2)
    b = sqrt(y**2-mid**2)
    return a*b/(a+b)


result = 0
#오차가 10**-3인데 c()에서 제곱을 취해줌
while end-start > 10**-6:
    mid = (start+end)/2
    if get_c(mid) >= c:
        result = mid
        start = mid
    else:
        end = mid

print("{}".format(round(result, 4))) #4번째 자리에서 반올림
