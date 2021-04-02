# step 1.
# 1-1. 동영상의 시각 형태를 초의 형태로 바꾼다
# 1-2. 광고의 시각 형태를 초의 형태로 바꾼다
# step 2.
# 2-1. total_time이라는 메모라이제이션을 위한 베열을 생성해준다
# 2-2. logs 배열내의 시작-종료 시각을 둘다 초로 만들어 준 뒤 시작 시간에는 시청자의 수를 +1 해주고 종료 시간에는 -1해준다
# step 3.
# 2번 과정으로 해둔 start,end 체크를 바탕으로 모든 구간에 시청자수를 기록한다
# total_time[i] = total_time[i] + total_time[i-1]
# i-1부터 i까지 1초 동안의 시청자의 수
# 000010000-100
# 000011111 000
# step 4.
# 모든 구간의 시청자를 누적 기록한다(step3의 반복작업)
# total_time[i] = total_time[i] + total_time[i-1] 
# 0부터 i까지 누적 시청자의 수
# 1 1 2 2 2 2  2  2  1  1
# 1 2 4 6 8 10 12 14 15 16
# step 5.
# most_view = total_time[i] - total_time[i - adv_time]
# 반복
# 반복문을 통해 가장 시청자수가 많은 구간을 탐색
# 구간대비 시청자수가 가장 많은 곳을 찾는다
# 현재 i의 누적 시청자수에서 i - adv_time의 누적 시청자 수를 빼면 해당 구간의 시청자 수 값을 얻음
#
def str_to_int(time):
    h,m,s = time.split(':')
    return int(h)*3600 + int(m) * 60 + int(s)
def int_to_str(time):
    h = time//3600
    h = '0'+ str(h) if h<10 else str(h)
    time %=3600
    m=time//60
    m = '0'+ str(m) if m<10 else str(m)
    time%=60
    s = '0'+ str(time) if time<10 else str(time)
    return h+':'+m+':'+s
def solution(play_time, adv_time, logs):
    answer = ''
    # 1
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    total_time = [0 for i in range(play_time+1)]
    print(play_time)
    print(adv_time)
    # 2
    for log in logs:
        start,end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
        total_time[start]+=1
        total_time[end]-=1
    # 3
    for i in range(1,len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
    # 4
    for i in range(1,len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
    most_view = 0
    max_time = 0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i-adv_time]:
                most_view = total_time[i] - total_time[i-adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time + 1 

    return int_to_str(max_time)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))