# https://www.acmicpc.net/problem/2230
# 이 문제는 투포인터 문제이다
# 배열에서 두수간의 차이값 구하기 -> 투포인터
import sys
n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
# 배열에 정렬을 하지 않으면 투 포인터를 쓸 수 없다
arr.sort()

start = 0
end = 1
ans = sys.maxsize

#1. arr[end] - arr[start]가 m보다 작을 경우 두 차이를 늘려줘야 한다 => end+1
#2. arr[end] - arr[start]가 m보다 크다면 m 보다 작은 최솟 값을 구해야 하므로 두 차이를 줄여준다 => start+1
#3. arr[end] - arr[start]가 m이라면 바로 출력
while end<n:
    tmp = arr[end] - arr[start]
    if tmp == m:
        print(m)
        sys.exit()
    elif tmp < m: # 음수가 나오거나 작을 수 있음을 커버해준다
        end+=1
        continue
    start += 1
    ans = min(tmp,ans)
          
print(ans) 

