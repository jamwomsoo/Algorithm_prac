# 정규식문제(Regular Expression)
# 정규식 참고 사이트
# https://whatisthenext.tistory.com/116
import re
def solution(word, pages):
    word = word.lower()
    urlToIdx = {} # key값 Url, value 인덱스 
    urlToScore = {} # key url, value [기본점수, 외부링크 수]
    urlToEnLink = {} # key url, value [해당 웹페이지로 링크가 걸린 다른 웹페이지]
    for i in range(len(pages)):
        lowerpage = pages[i].lower()
        # 정규식을 통해 해당 해당 홈페이지의 URL을 뽑아낸다
        # r'<meta[^>]*content="https://([\S]*)"/>'
        # -> r'<meta(^>가 아닌 다른 문자 중 0개 이상)content="https://([\S]*)"/>'
        # search 는 특정 문자들 사이에 있는 어떠한 문자열을 찾을때 쓰면 유용하다.
        # "https://(찾고자하는 문자열 그룹1번)"  에서 그룹 1번을 String 으로 반환해준다.
        # ->a.com
        # r은 \를 일반 문자로 보게 하기 위해서
        own_url = re.search(r'<meta[^>]*content="https://([\S]*)"/>',lowerpage).group(1)
        
        urlToIdx[own_url] = i
        word_cnt = 0
        # 기본점수를 위해 평문 여러개로 되어있는 것(단어) 중 word와 같은 것 만 추출
        for find in re.findall(r'[a-z]+',lowerpage):
            if find == word:
                word_cnt+=1
        s = set()
        # findall은 '<a href="https:// ">' 형식의 문자열을 뽑아서 리스트로 만들어줌
        for href in re.findall(r'<a href="https://[\S]*">',lowerpage):
            s.add(re.search(r'"https://([\S]*)"',href).group(1))
        s = list(s)
        urlToScore[own_url] = []
        # 기본 점수
        urlToScore[own_url].append(word_cnt)  
        # 외부 링크 수
        urlToScore[own_url].append(len(s))

        for e in s:
            if e not in urlToEnLink:
                urlToEnLink[e] = []
            urlToEnLink[e].append(own_url)
    result = []
    for key,value in urlToScore.items():
        match_score = value[0] 
        if key in urlToEnLink:
            for enUrl in urlToEnLink[key]:
                match_score+=urlToScore[enUrl][0]/urlToScore[enUrl][1]
        result.append([match_score,urlToIdx[key]])
    result.sort(key = lambda x : (-x[0],x[1]))
    answer = result[0][1]

    return answer
print(solution("blind",["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))