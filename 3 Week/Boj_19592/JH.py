# 장난감 경주

def time(speed, boost, x):
    s = ((x - boost) / speed) + 1 # 도착 하는 데 걸리는 시간 = (거리 - 부스터 거리) / 자신 속도) + 1(부스터 1초)
    return s

T = int(input())

for _ in range(T):
    n, x, y = map(int, input().split()) # n = 참가자, x = 거리, y = 부스터 사용 거리
    array = list(map(int, input().split())) # 참가자 속도 리스트
    fast = max(array[:n - 1]) # 가장 빠른 참가자 속도
    if fast < array[-1]: # 가장 빠른 참가자 보다 자신의 속도가 빠른 경우
        print(0) 
    else:
        s = x / fast # 가장 빠른 참가자가 도착 하는 데 걸리는 시간
        start = 0
        end = y
        while start <= end: 
            mid = (start + end) // 2 # 중간 값
            my = time(array[-1], mid, x) # 자신의 도착 하는 데 걸리는 시간
            if my >= s: # 자신의 시간이 참가자 시간보다 느리거나 같은 경우
                start = mid + 1 
            else: # 자신의 시간이 참가자 시간보다 빠른 경우
                end = mid - 1
        
        if start > y:
            print(-1)
        else:
            print(start)
