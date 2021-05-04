# 백준 사이트 https://www.acmicpc.net/problem/1377
# 참고 사이트 https://infinitt.tistory.com/229
# 풀이 정렬전의 요소들의 인덱스 값과, 정렬 후의 요소들의 인덱스 값을 비교하면 버블 정렬시에 몇 단계를 거쳤는지 알 수 있다
# 정렬 후 (1, 1)  (2, 3) (3, 4) (5, 2) (10, 0)
# 정렬 전 (10, 0) (1, 1) (5, 2) (2, 3) (3,  4)
# -----------------------------------------------
#           1      2     2       -1     -4
# 최대 값인 2에 1을 더하면 정답인다
a= []
n = int(input())
for i in range(n):
    a.append([int(input()),i])
b = sorted(a)
ans =[]
for i in range(n):
    ans.append(b[i][1] - a[i][1])

print(max(ans)+1) 


