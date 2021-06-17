# 백준 사이트 : https://www.acmicpc.net/problem/13397

# 백준 난이도 골드 3 인데 너무 어렵다...
# 구간을 나눌 때 각 구간의 (최대값-최솟값) 중에서 최대값이 해당 구간들을 나눴을때의 최댓값이다
# 이렇게 구간을 나눌 때 최대값들중에서 그 중 최솟값을 구해야 된다
# {각 구간의 (최대값 - 최소값)의 최대값}`s 최솟값을 ans이라고 할때
# 시작값을 0, 최대값을 (배열의 최대 - 배열의 최소)로 설정하고 mid를 구하며 이진 검색을 시작한다

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr) - min(arr)
# 함수를 시작할때 arr[0]을 하나의 구간으로 보고 시작한다
# ans가 최소값이므로 ans보다 나머지 구간들의 (최대값 - 최소값)의 최대값들은 ans보다 작을 값들로만 이루져야 한다 
# 만약 ans보다 큰 값이 나오면 해당 인덱스 전까지 구간을 끝내고 따로 구간을 만들어 해당 인덱스부터 다시 구간을 정해준다
def check(x):
    cnt = 1
    min_x= max_x = arr[0]
    for i in range(n):
        min_x = min(min_x, arr[i])
        max_x = max(max_x, arr[i])
        if max_x - min_x > x:
            cnt+=1
            min_x = arr[i]
            max_x = arr[i]
    return cnt
ans = start 
# 구간들의 갯수가 제한된 구간보다 크다는 것은 ans를 너무 작게 잡았다는 것이다
# ans를 키워줘야 한다
# 구간들의 갯수보다 제한된 구간의 갯수가 작다는 것은 ans를 너무 크게 잡았다는 것이다 
while start <= end:
    mid = (start + end)//2
    print(mid)
    if check(mid) <= m  :
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

print(ans)