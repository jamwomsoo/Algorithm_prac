# 모름+틀림
# 백준 사이트 : https://www.acmicpc.net/problem/13904
# 해설 사이트 : https://kkk4872.tistory.com/138
# 풀이
# 1. 점수를 기준으로 내림차순(1) + 점수가 같다면 마감기간으로 오름차순 정렬을 한다
# 2. 큐가 빌 때까지  큐의 앞에서부터 pop()
# 3. while 문 내부에서 방금 큐로부터 pop된 배열의 day에서부터 1일까지 내려가면서 날짜에 문제를 풀었는지 확인하는 배열의 해당 칸(인덱스)이 비어있는 지 확인
# 3-1. 만약 비어있으면 해당 일자에 문제를 풀수 있다(정답에 더해준다)
# 3-2. 만약 비어있지 않으면 해당 일자에는 이미 문제를 풀고있다는 뜻
#      -> 날짜를 앞으로 땡겨가면서 문제를 풀지 않은 날이 있는지 확인한다.
#      -> 그러다 빈날이 있으면 해당 일에 문제를 풀어준다
#    ==> 마감일은 지나면 못풀기때문에 뒤에서부터 앞에 날짜로 이동하면서 체크해야됨을 알자
# ans를 출력
import heapq
n = int(input())
q = []
last = 0
for i in range(n):
    d, w = map(int ,input().split())
    last = max(last,w)
    heapq.heappush(q,[-w,d,w])
index = 0
ans = 0
arr = [0]*(10000+1)# 총 과제를 할수있는 날의 수를 max로 잡는다(1,2,3,4,5,....,1000일수 있으니)
while q:
    a,day,value = heapq.heappop(q)
    
    for i in range(day,0,-1):
        if arr[i] == 0:
            arr[i] = value
            ans+=value
            break 
print(ans)