def solution(brown, yellow):
    answer = []
    total = brown+yellow
    arr = []
    for i in range(3,total//2 + 1):
        if total%i == 0 and total//i>=i:
            arr.append([total//i,i])

    #print(arr)
    if len(arr) == 1:
        return arr[0]
    else:
        for hori,ver in arr:
            if hori*2 + (ver-2)*2 == brown:
                return [hori,ver]
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))