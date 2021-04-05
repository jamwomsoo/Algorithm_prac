def check_section(time, lines):
    start_time = time
    end_time = time+1000
    cnt = 0
    for s,e in lines:
        # 궁금한 부분의 시작 부분이 원래 기준의 종료부분 보다 작아야됨
        #--------want-----------end------
        # 궁금한 부분의 끝 부분이 원래 기준의 시작 부분 보다 커야됨
        #---------start-----------end---------
        # 그럼 사이에 포함 된다고 볼 수 있다
        if e>=start_time and s<end_time:
            cnt+=1
    return  cnt
def solution(lines):
    answer = 0
    li = []
    # 시간을 모두 초로 바꿈 (0.001)초도 있으니 1000을 곱해준다
    for index, line in enumerate(lines):
        tmp = list(map(str,line.split(' ')))
        s = tmp[1].split(':')
        t = float(tmp[2].replace('s',''))*1000
        end =  (int(s[0])*3600 + int(s[1])*60 + float(s[2]))*1000
        start = end - t + 1
        li.append([start,end])
    # 요청량이 변하는 순간은 각 로그의 시작과 끝뿐임
    # -> 초당 최대 처리량은 각
    for start,end in li: 
        answer = max(answer, check_section(start,li),check_section(end,li)) 
    return answer
print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution( [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

))