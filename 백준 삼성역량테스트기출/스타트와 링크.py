from itertools import permutations
from itertools import combinations
n = int(input())
arr= []
people = [i+1 for i in range(n)]
start = list(combinations(people,n//2))

for i in range(n):
    arr.append(list(map(int, input().split())))

def func(array):
    _sum = 0
    for x,y in array:
        _sum += arr[x-1][y-1]
    return _sum


gap = (int(1e9))
for com in start:
    link = [i for i in range(1,n+1) if i not in com]
    start_coms = list(permutations(com,2))
    link_coms = list(permutations(link,2))
    gap = min(gap,abs(func(start_coms) - func(link_coms)))

print(gap)
