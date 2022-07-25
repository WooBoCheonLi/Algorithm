n = int(input()) # 점의 개수 n
a,b = map(int, input().split()) # 가로 a 세로 b

ans = 0 
arr = []
for i in range(n): # 점의 좌표
    arr.append(tuple(map(int, input().split())))

for p1 in arr:
    p2 = (p1[0] +a, p1[1]) # 우측하단
    p3 = (p1[0], p1[1] +b) # 좌측상단
    p4 = (p1[0]+a, p1[1]+b) # 우측 상단

    if p2 in arr and p3 in arr and p4 in arr:
        ans += 1
print(ans)


# def binary_search(arr, start, end, target):
#     while start <= end:
#         mid = (start+end)//2
#         if target == arr[mid]:
#             return True
        
#         elif target > arr[mid]:
#             end = mid-1
#         elif target < arr[mid]:
#             start = mid+1
          