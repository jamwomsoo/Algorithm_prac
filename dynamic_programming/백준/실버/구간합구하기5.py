# 못품
# 백준 사이트 : https://www.acmicpc.net/status?user_id=tjdtn4806&problem_id=11660&from_mine=1
# 풀이 사이트 : https://velog.io/@ready2start/Python-%EB%B0%B1%EC%A4%80-11660-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-5


# prefix sum 문제이다(구간합) + 이차배열
# 알고리즘
# 1. 행 별로 prefid_sum을 해줌
# 2. 행을 prefix_sum 한 상태에서 열로 prefix_sum 해준다
# 3. A | B
#    C | D
#   D 구역에 속한 수들의 합만을 구하기 위해서는  (A + B + C + D) - (A + C) - (A + C) + A를 해줘야한다
#   결론적으로 D까지의 Prefix_sum - (A+C)구간의 prefix_sum - (A+B)구간의 prefix_sum + A 구간의 prefix_sum을 해주면됨
# 공식화 => ((x1,y1) ~ (x2,y2)의 구간합은) = dp[x2][y2] -dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]이다
#  
# 
# 무조건 stdin.readline().split() 써야 풀림
from sys import stdin


n, m = map(int, stdin.readline().split())

numbers = [[0] * (n + 1)]

for _ in range(n):
    nums = [0] + [int(x) for x in stdin.readline().split()]
    numbers.append(nums)

# prefix sum 행렬 만들기

# 행 별로 더하기
for i in range(1, n + 1):
    for j in range(1, n):
        numbers[i][j + 1] += numbers[i][j]

# 열 별로 더하기
for j in range(1, n + 1):
    for i in range(1, n):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])