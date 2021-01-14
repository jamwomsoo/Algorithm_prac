import bisect
def count_by_range(arr,left_value,right_value):
    right = bisect.bisect_right(arr,right_value)
    left = bisect.bisect_left(arr,left_value)
    return right - left


def solution(words, queries):
    answer = []
    arr=[[] for _ in range(10001)]
    reverse_arr=[[] for _ in range(10001)]
    
    for word in words:
        arr[len(word)].append(word)
        reverse_arr[len(word)].append(word[::-1])
    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()
    # fro?? 라는 쿼리일때, count_by_range()함수를 이용하여 froaa가 들어갈 위치(맨앞) frozz가 들어갈 위치(맨뒤)를 찾아서 fro?? 개수를 리턴
    # ?가 접두사를 등장하면 비교가 불가능 하기 때문에 쿼리와 단어들을 뒤집어서 비교한다
    for q in queries:
        if q[0] == '?': # 접두사에 ? 있음
            answer.append(count_by_range(reverse_arr[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z')))
        else:
            answer.append(count_by_range(arr[len(q)], q.replace('?','a'), q.replace('?','z')))
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))
#print(solution(["ff","FFFFF","o"],["?","?","?????"]))