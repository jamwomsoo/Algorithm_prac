# 2 4 5 7 9 가 주어 졌을때
# 간격간 최대값이 최소가 되기 위해서는
# 2 5 9 7 4 와 같이 가운데 가장 큰값을 두고
# 양 옆으로 다음으로 작은 숫자들을 채워 넣으면 된다
# 이렇게 정렬 시킨 배열가의 사이값은
# 일반적으로 정렬 후 현재 인덱스에서 두개 앞에 있는 인덱스를 빼는 것과 같다 
for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = []
    arr.sort()
    result = arr[1]-arr[0]
    for i in range(n):
        if i+2 <= n-1:
            result = max(result,arr[i+2]-arr[i])
    print(result)
    
