# n 참가자 수
# x 거리
# y 부스터 최대치
# V 참가자 별 속도

# 시간 = 거리 / 속도

T = int(input())


for i in range(T):
    n,x,y = map(int, input().split())
    V = list(map(int, input().split()))

    if V[-1] == max(V): #내 일반속도가 가장 빠른 경우
        print(0)
        continue

    #V[-1] # 나의 일반속도
    #max(V) # 1등의 일반속도

    # 최소 시간 target
    target_time = x/max(V)

    arr  = [i for i in range(y+1)] #사용가능한 부스터의 속도


    #부스터만 써서 들어올 때
    ans = y+1
    start = 0
    end = y

    while start <= end:
        mid = (start + end)//2 

        # 부스터의 속도 = 부스터로 간 거리 
        boost = arr[mid] 
        # 내가 걸리는 시간 x
        me = (x-boost)/V[-1] + 1 # (총거리-부스터로간거리)/원래속도 + 1(부스터로 시간) = 총 시긴


        if me < target_time: # 더 일찍 들어왔다면
            ans = min(ans, boost)
            end = mid -1 #부스터 속도를 줄여보기
        else:
            start = mid+1 #부스터 속도를 높이기
    
    if ans == y+1:
        print(-1)
    else:
        print(ans)

        
