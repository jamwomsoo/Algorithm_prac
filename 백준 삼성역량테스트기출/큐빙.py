from copy import deepcopy
import sys
input = sys.stdin.readline

def rotate(c):
    global L,R,U,D,F,B
    t,X,Y,Z,W = F,U,L,D,R
    new_arr = deepcopy(F)
    if c == 'B':
        t,X,Y,Z,W = B,R,D,L,U
        new_arr = deepcopy(B)
    if c == 'U':
        t,X,Y,Z,W = U,L,F,R,B
        new_arr = deepcopy(U)
    if c == 'D':
        t,X,Y,Z,W = D,B,R,F,L
        new_arr = deepcopy(D)
    if c == 'L':
        t,X,Y,Z,W = L,F,U,B,D
        new_arr = deepcopy(L)
    if c == 'R':
        t,X,Y,Z,W = R,D,B,U,F
        new_arr = deepcopy(R)
    
    for i in range(3):
        for j in range(3):
            new_arr[j][3-i-1] = t[i][j]
    if c == 'F':
        F = new_arr
    if c == 'B':
        B = new_arr
    if c == 'U':
        U = new_arr
    if c == 'D':
        D = new_arr
    if c == 'L':
        L = new_arr
    if c == 'R':
        R = new_arr
            
    X[2][2],X[2][1],X[2][0],Y[2][0],Y[1][0],Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2]=\
        Y[2][0],Y[1][0],Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2],X[2][2],X[2][1],X[2][0]

for _ in range(int(input())):
    U = [['w']*3 for _ in range(3)]
    F = [['r']*3 for _ in range(3)]
    L = [['g']*3 for _ in range(3)]
    R = [['b']*3 for _ in range(3)]
    D = [['y']*3 for _ in range(3)]
    B = [['o']*3 for _ in range(3)]
    n = int(input())
    sequnce = list(map(str, input().split()))

        
    for area, direct in sequnce:
      
        rotate(area)
        if direct == '-':
            rotate(area)
            rotate(area)
    for i in range(3):
        print("".join(j for j in U[i]))
# def clockwise(arr): # 시계방향으로 k번 만큼 회전
#     tmp = arr[0][0]
#     arr[0][0] = arr[2][0]
#     arr[2][0] = arr[2][2]
#     arr[2][2] = arr[0][2]
#     arr[0][2] = tmp
 
#     tmp = arr[0][1]
#     arr[0][1] = arr[1][0]
#     arr[1][0] = arr[2][1]
#     arr[2][1] = arr[1][2]
#     arr[1][2] = tmp
 
# def U(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[0])
#         tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
#         cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
#         cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
#         cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
#         cube[3][0][2], cube[3][1][2], cube[3][2][2] = tmp
 
# def D(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[2])
#         tmp = cube[4][0][2], cube[4][1][2], cube[4][2][2]
#         cube[4][0][2], cube[4][1][2], cube[4][2][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
#         cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[3][2][0], cube[3][1][0], cube[3][0][0]
#         cube[3][2][0], cube[3][1][0], cube[3][0][0] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
#         cube[5][0][0], cube[5][0][1], cube[5][0][2] = tmp
 
# def R(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[4])
#         tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
#         cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
#         cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
#         cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
#         cube[5][0][2], cube[5][1][2], cube[5][2][2] = tmp
 
# def L(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[3])
#         tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
#         cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[5][0][0], cube[5][1][0], cube[5][2][0]
#         cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
#         cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
#         cube[1][0][0], cube[1][1][0], cube[1][2][0] = tmp
 
# def F(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[1])
#         tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
#         cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
#         cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][0][2], cube[2][0][1], cube[2][0][0]
#         cube[2][0][2], cube[2][0][1], cube[2][0][0] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
#         cube[4][2][0], cube[4][2][1], cube[4][2][2] = tmp
 
# def B(c):
#     if c == '+':
#         k = 1
#     else:
#         k = 3
#     for _ in range(k):
#         clockwise(cube[5])
#         tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
#         cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
#         cube[4][0][0], cube[4][0][1], cube[4][0][2] = cube[2][2][2], cube[2][2][1], cube[2][2][0]
#         cube[2][2][2], cube[2][2][1], cube[2][2][0] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
#         cube[3][0][0], cube[3][0][1], cube[3][0][2] = tmp
 
# from copy import deepcopy
 
# CUBE = [[[] for _ in range(3)]for _ in range(6)]
 
# # 큐브 초기화
# s = 'wrygbo' # U F D L R B
# for i in range(6):
#     for j in range(3):
#         for _ in range(3):
#             CUBE[i][j].append(s[i])
 
 
# for _ in range(int(input())):
#     n = int(input())
#     cmd = input().split()
#     cube = deepcopy(CUBE)
 
#     while cmd:
#         c = cmd.pop(0)
#         if c[0] == 'L':
#             L(c[1])
#         elif c[0] == 'D':
#             D(c[1])
#         elif c[0] == 'U':
#             U(c[1])
#         elif c[0] == 'F':
#             F(c[1])
#         elif c[0] == 'R':
#             R(c[1])
#         elif c[0] == 'B':
#             B(c[1])
 
#     for i in range(3):
#         print(''.join(cube[0][i]))
