# https://www.acmicpc.net/problem/16208
n = int(input())
arr = list(map(int, input().split()))
result = 0
total = sum(arr)

# n개의 막대기가 필요
# 총 n개의 모든 막대기들이 합쳐져 있는 값은 T
# 답을 구하려면 a1 * (T-a1) + a2 * (T-a1-a2) + a3 * (T-a1-a2)
# -> a1 * (a2+a3) + a2 * (a3) + a3 * (0)
# -> a1a2 + a1a3 + a2a3
# 이를 통해 각가의 막대기가 서로 곱해져있는 것을 확인 가능
# 어느 순서로 잘라도 비용은 모두 같게 된다

for i in range(n):
    tmp = arr[i]
    total-=tmp
    result += total*tmp
print(result)
