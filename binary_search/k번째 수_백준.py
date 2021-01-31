# 인덱스가 1부터 시작하는 arr[i][j] = i*j인 배열에서 k번째 원소 찾기
# 예) 3 x 3인 배열일때
# 1 2 3
# 2 4 6
# 3 6 9
# 1 이하의 수 1개
# 2 이하의 수 3개
# 3 이하의 수 5개
# 4 이하의 수 6개
# 5 이하의 수 6개
# 6 이하의 수 8개
# 7 이하의 수 8개
# 8 이하의 수 8개
# 5이하는 6개 이고 6이하의 수는 8개 이므로 6은 2개 있다는 말이다  
# 6이하는 8개이고 7이하는 8개 인데 이말은 즉, 7은 없다는 것이다   
# 어떠한 수 x가 배열에 존재하는지 안하는지는
# 배열내의 x이하의 원소의 개수 - 배열내의 (x-1)이하의 원소의 개수가 0인지 아닌지 보면 알 수 있다  


n = int(input())
k = int(input())

start = 1
end = k
ans = 0
while start <= end:
    mid = (start + end)//2
  
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n, mid//i )
    if cnt>=k:
        ans = mid
        end = mid - 1
    else: 
        start = mid +1
print(ans)
