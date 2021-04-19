# https://www.acmicpc.net/problem/2343
# 못품
# 참고 https://deok2kim.tistory.com/109
# start = max(arr) = 9로 하는 이유 -> 각자 한개의 블루레이를 갖고있을경우->10개
# end = sum(arr) = 45로 하는 이유 -> 하나의 블루레이만 갖고 있을 경우

def add_lesson(arr,mid):
    global n,m
    cnt = 0
    sum_lesson = 0
    for i in range(n):
        if sum_lesson+arr[i]>mid:
            cnt+=1
            sum_lesson = 0
        sum_lesson+=arr[i]
    else:
        if sum_lesson:
            cnt+=1
    return cnt

def binary_search(arr,start,end):
    global n,m
    while start<=end:
        mid = (start+end)//2
        cnt = add_lesson(arr,mid)
        if cnt<=m:
            end = mid - 1
        else:
            start = mid+1
    return start

n, m = map(int, input().split())
arr = list(map(int, input().split()))

print(binary_search(arr,max(arr),sum(arr)))
