def timeToSec(start,end):
    
    start = list(map(int,start.split(':')))
    end = list(map(int, end.split(':')))
    start = start[0]*60+start[1]
    end = end[0]*60 + end[1]
    return end - start
def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    dic = {}
    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')
       
        time = timeToSec(start,end)
        melody = melody.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    
        melody = melody*(time//len(melody)) + melody[0:time%len(melody)]
        dic[name] = melody
    answer = ["",""]
    
    for key, value in dic.items():
        if m in value:
            if len(answer[1])<len(value):
                answer[0] = key
                answer[1] = value
    return "(None)" if len(answer[0]) == 0 else answer[0]
#print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",	[ "04:00,04:08,BAR,CC#BCC#BCC#B"]))