def check(m,stones,k):
    cnt = 0
    s = [i-m for i in stones]
    for i in s:
        if i<=0: 
            cnt+=1
            if cnt >= k:
                return False
        else:
            cnt = 0
    return True
def solution(stones, k):
    end = max(stones)
    answer = start = min(stones)
    while start<=end:
        mid = (start+end)//2
        jugde = check(mid,stones,k)
        if jugde:
            start = mid + 1
            answer = max(start,answer)
        else:
            end = mid - 1
    return answer
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))