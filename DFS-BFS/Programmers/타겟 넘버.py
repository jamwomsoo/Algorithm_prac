# 배열 맨 앞부터 인덱스를 돌면서 -일때, + 일때로 케이스를 나누어서 dfs로 완전탐색한다
from copy import deepcopy
def dfs(numbers, target, cnt, n):
    if cnt == n:
        if sum(numbers) == target:
            return 1
        return 0
    changed_numbers = deepcopy(numbers)
    changed_numbers[cnt] = -(changed_numbers[cnt])
    return dfs(numbers,target,cnt+1,n) + dfs(changed_numbers,target,cnt+1,n)

def solution(numbers, target):
    n = len(numbers)
    answer = dfs(numbers,target,0,n)
    return answer
print(solution([1, 1, 1, 1, 1],3))