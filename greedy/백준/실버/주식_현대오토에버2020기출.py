# 백준 사이트 : https://www.acmicpc.net/problem/11501
# 배열의 역순으로 돌기 시작하면서 매 순간의 최댓값에서 현재 인덱스의 값 뺀값을 모두 더한다

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    result =0
    max_value = -int(1e9)
    for i in range(n-1,-1,-1):
        max_value = max(max_value,arr[i])
        result+=max_value - arr[i]
        
    print(result)
            