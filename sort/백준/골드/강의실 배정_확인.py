# 못품
# https://www.acmicpc.net/problem/11000
import heapq
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort()
cnt = 1

end = [arr[0][1]]
# 강의 시작 시간별로 정렬된 배열에서
# 종료시간(우선순위 큐로 되어있어 맨 첫번째는 가장 빨리 끝나는 시간이다)보다 시작시간이 빠르면 새로운 강의실을 추가해주고
# 아니라면 해당 강의실의 종료 시간을 바꾼다
index = 0
for i in range(1,n):
    # 강의실 종료시간보다 시작시간이 늦거나 같으면
    # 기존의 종료시간을 제거하고 새로운 종료시간을 넣어준다 
    if end[0] <= arr[i][0]:
        heapq.heappop(end)
        heapq.heappush(end,arr[i][1])
    # 강의실 종료시간보다 시작시간이 빠르면
    # -> 새로운 강의실을 추가(종료 시간)
    else:
        heapq.heappush(end,arr[i][1])

    

print(len(end))