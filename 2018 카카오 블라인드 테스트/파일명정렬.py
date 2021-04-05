def files_sort(files):
    arr = []
    files.sort(key = lambda x : (x[0],x[1]))

    return files

def solution(files):
    answer = []
    f = files.copy()
    for index, _file in enumerate(files):
        num = ''
        head = ''
        tmp = ''
        idx = 0
        for i in range(len(_file)):
            if _file[i].isdecimal():
                break
            head+=_file[i]
            idx+=1
        cnt = 0
        for i in range(idx,len(_file)):
            if not _file[i].isdecimal():
                break
            if cnt>=5: break
            num+=_file[i]
            idx+=1
        
        files[index] = [head.lower(),int(num),_file]
    answer = files_sort(files)
    #print('head,num,tail',files)
    answer = [x[-1] for x in files ]
    
    return answer
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "b-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
#print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
#print(solution([  "IMg10.png","img10.png", "Img10.png",]))