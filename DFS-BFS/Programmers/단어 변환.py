import sys
sys.setrecursionlimit(100000)
answer = int(1e9)
visited = []
def find_diff(begin,i):
    n = len(i)
    diff = 0
    for j in range(n):
        if begin[j] != i[j]:
            diff+=1
    return diff
def dfs(begin,target,words,cnt):
    global answer
    visited.append(begin)
    if begin == target:
        answer = min(answer, cnt)
        return
    arr = []
    for i in words:
        diff = find_diff(begin,i)
        if diff == 1 and i not in visited:
            arr.append(i)
    for i in arr:
        dfs(i,target,words,cnt+1)
def solution(begin, target, words):
    if target not in words:
        return 0
    dfs(begin,target,words,0)
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]	))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))

# 다른 사람 풀이
# 큐에 현재 단어부터 차이가 1나는 다른 단어들을 모두 완전 탐색한다
# from collections import deque


# def get_adjacent(current, words):
#     for word in words:
#         if len(current) != len(word):
#             continue

#         count = 0
#         for c, w in zip(current, word):
#             if c != w:
#                 count += 1

#         if count == 1:
#             yield word


# def solution(begin, target, words):
#     dist = {begin: 0}
#     queue = deque([begin])

#     while queue:
#         current = queue.popleft()

#         for next_word in get_adjacent(current, words):
#             if next_word not in dist:
#                 dist[next_word] = dist[current] + 1
#                 queue.append(next_word)

#     return dist.get(target, 0)