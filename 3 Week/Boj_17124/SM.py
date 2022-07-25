# A : n 개의 정수
# B : m 개의 정수

# C : 길이가 n 인 배열

from bisect import bisect_right

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    A = tuple(map(int, input().split()))  # 20 5 14 9
    
    B = list(map(int, input().split()))  # 16 8 12
    B.sort() # 정렬

    # C = 16, 8, 12, 8

    # 이것은 다시 말해 A[i] 가 B의 index 에 넣은 뒤 그 왼쪽 값을 반환
    C = 0
    for i in A:   
        c = bisect_right(B, i) # i 가 들어가는 index   #################지금 단순히 가까운애가 아니라 왼쪽애만 데려오고 있음
    
        if c == 0:
            C += B[c] # 오른쪽 수

        elif c == len(B):
            C += B[c-1]

        else:
            
            if ((i- B[c-1])) <= (B[c]-i): # 왼쪽이 더 가깝다면
                C += B[c-1]
            else:
                C += B[c] 

    print(C)
    

    


