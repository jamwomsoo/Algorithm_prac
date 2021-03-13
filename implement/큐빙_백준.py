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