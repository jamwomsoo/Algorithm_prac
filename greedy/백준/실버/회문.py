import sys
sys.setrecursionlimit(100000)
n = int(input())

def is_semi_pal(start,end,skip):
    if start>end: return 1
    if p[start] == p[end]: return is_semi_pal(start+1,end-1,skip)
    elif skip:
        #print("ss",is_semi_pal(start+1,end,0),is_semi_pal(start,end-1,0))
        return max(is_semi_pal(start+1,end,0),is_semi_pal(start,end-1,0))
    else: return 0
    
def is_pal():
    global _len
    if _len%2 == 0:
        tmp = p[_len//2:]
        if p[:_len//2] == tmp[::-1]:
           return True
    if _len%2 == 1:
        tmp = p[_len//2:]
        if p[:_len//2+1] == tmp[::-1]:
            return True
    return False

def get_ans():
    global _len
    if is_pal(): return 0
    elif is_semi_pal(0,_len-1,1): return 1
    else: return 2
for _ in range(n):
    p = list(map(str, input()))
    _len = len(p)
    print(get_ans())
    
   
    