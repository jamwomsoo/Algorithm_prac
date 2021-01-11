################################################
# 2차원 리스트를 90도 회전한 결과를 반환 하는 함수
################################################
def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result
#################################################

