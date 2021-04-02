def rebuild(board):
    m = len(board)
    n = len(board[0])
    
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if board[i][j] == 0: continue
            if i+1<m and board[i+1][j] == 0:
                d = i
                while True:
                    if d+1>=m:
                        break
                    if d+1<m and board[d+1][j] !=0:
                        break
                    if d+1<m and board[d+1][j] == 0:
                        d+=1
                board[d][j],board[i][j] = board[i][j],0
                
def remove(board,s):
    for x,y in s:
        board[x][y] = 0
    
def solution(m, n, board):
    answer = 0

    for i in range(m):
        board[i] = list(map(str,board[i]))
   
    while True:
        s = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j+1]:
                    s.add((i,j))
                    s.add((i+1,j))
                    s.add((i,j+1))
                    s.add((i+1,j+1))
        if len(s) == 0:
            break
        else:
            answer+=len(s)
        
        remove(board,s)

        rebuild(board)

    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"] ))