# 장난감 경주
'''
n : 참가자 수
x : 트랙의 길이
y : 가속도 한계치
v : 속도/ 마지막이 내 속도 

부스터를 사용해 이동해야 하는 최소한의 거리 구하기
안쓰고 우승 가능하면 0
써도 안되면 -1
'''
t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    v = list(map(int, input().split()))
    