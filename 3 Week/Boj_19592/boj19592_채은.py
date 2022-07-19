t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    v = list(map(int, input().split()))
    
    max_val = max(v)
    my_val = v[-1]
    
    if max_val == my_val:
        print(0)
    elif y <= max_val:
        print(-1)
    else:
        target = x - (x / max_val - 1) * my_val
        if int(target) + 1 > y:
            print(-1)
        else:
            print(int(target) + 1)