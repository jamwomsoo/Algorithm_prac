#내풀이_정답
from copy import deepcopy
def rotate_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
def solution(key, lock):
     
    arr = [[0]*len(lock)*3 for _ in range(len(lock)*3)]
    start = round(len(arr)//3)
    for i in range(len(lock)):
        for j in range(len(lock)):
            arr[i+start][j+start] = lock[i][j]
    
    for _ in range(4):
        for i in range(len(arr) - len(lock)+1):
            for j in range(len(arr) - len(lock) +1):
                a=deepcopy(arr)
                check = True
                for i2 in range(i,i+len(key)):
                    for j2 in range(j,j+len(key)):
                        a[i2][j2]+=key[i2-i][j2-j]
                for k in range(start,start+len(lock)):
                    for z in range(start,start+len(lock)):
                        if a[k][z]  != 1:
                            check = False
                            break  
                    if check == False:
                        break
                if check == True:
                    return True  
        key = rotate_90_degree(key)                
    return False
##############
#해설지 풀이
##############
# 2차원원 리스트 회전
def roatate_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result 
#새로 만든 리스트 중간에 기존 자물쇠를 두었기 때문에
#중간부분(자물쇠)이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True
def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 새로운 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0](n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key = roatate_90_degree(key) #열쇠 회전
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
