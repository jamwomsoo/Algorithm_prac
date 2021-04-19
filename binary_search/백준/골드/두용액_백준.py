import heapq
import sys
# 투 포인터로 양끝점에서 시작한다(first point, end point)
# 만약 두 포인터가 위치한 곳 들의 값의 합이 양수면 줄이기 위해 end point를 한칸 줄이다
# 음수 일때는 first point 값을 앞으로 늘린다
# 우선순위 큐에 두 포인터가 가리키는 값들의 합을 abs로 처리해 두 값의 차이가 제일 작은 값을 마지막에 뽑아낸다(우선순위 큐의 top) 
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
fp = 0
ep = n-1
q = []
flag = False
while fp < ep:
    print(q)
    if arr[fp] + arr[ep] > 0:
        heapq.heappush(q,[abs(arr[fp]+arr[ep]), arr[fp],arr[ep]])
        ep-=1
    elif arr[fp] + arr[ep] < 0:
        heapq.heappush(q,[abs(arr[fp]+arr[ep]), arr[fp],arr[ep]])
        fp+=1
    else:
        print(arr[fp],arr[ep])
        flag = True
        break 
if not flag:
    a = heapq.heappop(q)
    print(a[1], a[2])