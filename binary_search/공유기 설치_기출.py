# 두 공유기의 사이의 거리를 gap이라 하겠다
# 이 문제는 처음에 최소 gap과 최대 gap을 구해 각각 start end 로 둔다
# 이제 이진 탐색으로 가장 가까운 공유기 간 거리의 최대를 구하기 위해 
# 공유기 간 거리의 최소값을 이진함수로 찾아보자
# 예)
# 1 2 4 8 9 이렇게 있을때 공유기 3개
# step1. gap을 mid 값으로 넣고 앞에서 부터 공유기를 넣되 gap을 지키며 넣는다
# 1 8(5가 없으므로 그 이상 값)
# step2. 현재gap은 너무 크므로 end를 mid-1로 넣고 mid를 구하면 2(gap)이다, 위와 같이 다시 앞부터 gap을 지키며 넣으면
# 1 4(3이 없으므로 최소 거리 2를 지키며) 8(6이 없으므로 최소 거리 2를 지키며)
# step3. gap의 값을 증가시켜서 gap이 더 커졌을 때도 가능한지 보기 위해 start를 mid+1로 키워본다 mid = 3
# 1 4 8(7이 없으므로 최소 거리 3을 지키며)
# 이제 가장 이상적인 정답을 구했다 ==> 3 
n,c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
def binary_search():
    start = int(1e9)
    # 집 위치간 최소 거리 찾기
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            start = min(start, j-i)
    #집 위치간 최대 거리 찾기
    end = arr[-1] - arr[0]
    result = 0
    while start <= end:
        cnt=1
        value = arr[0] 
        mid = (start+end)//2
        for i in arr:
            if i >= mid+value:
                value = i
                cnt+=1
        
        if cnt <c:# 공유기가 c개 보다 작으면 거리를 감소
             end = mid-1
        else:# 공유기가 c개 이상 설치 가능 할때 거리를 증가
            start = mid+1
            result = mid
    return result
print(binary_search())

                
        
