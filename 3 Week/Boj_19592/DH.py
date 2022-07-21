#19592 장난감 경주

'''
입력)
n : 참가자 수
x : 트랙의 길이
y : 가속도 한계치
v : 속도/ 마지막 값= 내 속도 
z= 우승이 가능토록하는 최소값 
출력)
1.안쓰고 우승 가능하면 0
2. if 우승가능 =>최소 부스터 사용  거리 
   else  -1
구현)
v[-1]을 제외한 최대 속력을 구해서 걸리는 시간을 구함
(트랙의 길이 -부스터로 간거리)/기본 속력 +1(부스터로 간 시간)
start : 기본속력 m_res : 최소 시간 저장 end: 최대 속력
공동우승은 불가함으로  걸린시간은 Second_place 보다 작아야함
'''
for _ in range(int(input())):
  n,x,y=map(int,input().split())
  v=list(map(int,input().split()))
  Second_place=x/max(v[:-1]) 

  if Second_place> x/v[-1]:
    print(0)
    continue

  start, m_res,end=v[-1],0,y
  while start<=end:
    mid=(start+end)//2
    speed=((x-mid)/v[-1])+1
    if speed<Second_place:
      end=mid-1
      m_res=mid
    else:
      start=mid+1
  print(m_res if m_res>0 else -1)
