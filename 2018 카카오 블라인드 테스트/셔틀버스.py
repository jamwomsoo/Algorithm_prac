def turn_to_hour(second):
    hour = second//60
    second %=60
    if 0<=hour<10:
        hour= '0'+str(hour)
    else:
        hour = str(hour)
    if 0<=second<10:
        second ='0'+str(second)
    else:
        second = str(second)
    return hour+':'+second
def solution(n, t, m, timetable):
    answer = ''
    table = []
    dic={}
    for time in timetable:
        tmp = time.split(':')
        a = int(tmp[0])*60+int(tmp[1])
        table.append(a)
    table.sort()
    bus = [(540 +t*i,0,None) for i in range(n)]
    bus_index = crew_index = 0
    while crew_index<len(table):
        crew = table[crew_index]
        if bus_index == len(bus):
            break
        if crew<=bus[bus_index][0] and bus[bus_index][1]<m:
            second,member_cnt,last = bus[bus_index]
            bus[bus_index] = (second,member_cnt+1,crew)
            crew_index+=1
        else:
            bus_index+=1
    answer = bus[-1][0]
    if bus[-1][2]:
        if bus[-1][1] == m:
            answer = bus[-1][2]-1
    answer = turn_to_hour(answer)
    return answer
# print(solution(1,1,5,["08:00", "08:01", "08:02", "08:03"]))
# print(solution(2,10,2,["09:10", "09:09", "08:00"]))
# print(solution(2,1,2,["09:00", "09:00", "09:00", "09:00"]))
print(solution(1,1,1,	["23:59"]))
print(solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))