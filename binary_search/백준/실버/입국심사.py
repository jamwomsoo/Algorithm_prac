# https://www.acmicpc.net/problem/3079
# 틀림
# https://hsdevelopment.tistory.com/558 참고
# i 시간에 각 심사대에서 처리할 수 있는 명수의 합으로 구할 수 있다
# 만약 i 시간에 각 심사대에서 처리할 수 있는 명수들의 합이 m보다 크면
# end = mid-1
# 만약 m 보다 작으면 
# start = mid + 1
n,m = map(int, input().split())
arr =[int(input()) for _ in range(n)]
start = 0 ;end = max(arr)*m
ans = end
def binary_search(arr,start,end):
    global n,m,ans
    while start<=end:
        mid = (start+end)//2
        total = 0
        for i in range(n):
            total+=mid//arr[i]
        
        if total>=m:
            
            end = mid - 1
            ans = min(mid,ans)
        else:
            start = mid + 1
binary_search(arr,start,end)
print(ans)
