# 배열의 원소간 차이가 큰것부터 빼면서 k-1개 빼준다
# 예) 선을 3개 그으면 그룹은 4개
# k = 3 (3개의 그룹으로 묶을 때)
# 0 0| 0 0| 0 0 (2개의 선을 그으면 3개의 그룹이 되는 것과 같은 논리로 빼줌) 
n,k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = 0
gap = []
tmp  = [ ]
for i in range(n-1):
    gap.append(arr[i+1]-arr[i])
result = sum(gap)
gap.sort(reverse=True)

print(sum(gap)-sum(gap[:k-1]))