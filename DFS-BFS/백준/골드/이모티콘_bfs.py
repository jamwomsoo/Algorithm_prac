from collections import deque
import sys
time = 0
q = deque()
q.append([0,1,0])
s = int(input())
visited = {}
visited[(0,1,0)] = 1

while q:
    #print(q)
    t, emoticon_num,clip = q.popleft()
    if emoticon_num <0 :continue
    if emoticon_num == s:
        print(t)
        sys.exit()
    
    #print((t+1, emoticon_num, emoticon_num) not in visited.keys())
    if  (t+1, emoticon_num, emoticon_num) not in visited.keys() :
        q.append([t+1,emoticon_num,emoticon_num])
        visited[(t+1,emoticon_num,emoticon_num)] = 1
    
    if (t+1, emoticon_num+clip, emoticon_num) not in visited.keys():
        q.append([t+1,emoticon_num+clip,clip])
        visited[(t+1,emoticon_num+clip,emoticon_num)] = 1
    
    if (t+1,emoticon_num-1,emoticon_num) not in visited.keys():
        q.append ([t+1,emoticon_num-1,clip])
        visited[(t+1,emoticon_num-1,emoticon_num)] = 1
    