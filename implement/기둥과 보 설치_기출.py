#기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
#보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
#(x,y) a 0은 기둥, 1은 보 b => 0은 삭제, 1은 설치
#위쪽, 오른쪽
#매번 전체 구조물을 확인한다


def possible(answer):
    for i in answer:
        x,y,a = i
        if a == 0:#기둥일때
            #바닥위, 보의 양쪽 끝 중 하나 위
            if y == 0 or [x,y-1,0] in answer or [x-1,y, 1] in answer or [x,y,1] in answer:
                continue
            return False
        elif a==1:#보일때
            #양쪽 끝중 하나가 기둥, 양 옆이 보
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1, y, 1] in answer and [x+1,y,1] in answer):
                continue
            return False 
    return True
    
    

        
def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, a, b = i 
        if b == 1:#설치
            answer.append([x,y,a])
            if not possible(answer):
                answer.remove([x,y,a])
        else: # 삭제
            answer.remove([x,y,a])
            if not possible(answer):
                answer.append([x,y,a])
           
            
    answer = sorted(answer, key = lambda x : (x[0], x[1], x[2]))
    return answer
#print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5,[[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]))