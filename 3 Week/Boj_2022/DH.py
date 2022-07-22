from math import sqrt

x, y, c = map(float, input().split())
start, end = 0, min(x, y)
res = 0

def c(mid):
    a = sqrt(x**2-mid**2)
    b = sqrt(y**2-mid**2)
    return a*b/(a+b)



while end-start > 1e-6:
    mid = (start+end)/2
    if c(mid) >= c:
        res = mid
        start = mid
    else:
        end = mid

print("{}".format(round(result, 4)))
