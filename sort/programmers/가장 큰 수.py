def solution(numbers):
    answer = ''
    arr = list(map(str,numbers))
    # -> x * 3이 이문제의 핵심:
    # numbers의 각 원소 배열들을 number라고 할때 1부터 1000까지 이므로 각 자리 수가 안 맞을 수 있다
    # 이를 해결하기 위해 1000이 자리수가 3이므로(0,1,2,3)
    # x* 3을 하여 number의 문자열을 (0,1,2,3)인덱스?를 반복한다는 뜻
    # 예) 1, 1000일때 
    # 1, 1 비교 1,0 비교 1,0 비교 1,0비교
    # -> 1이 1000보다 높으수로 여겨져서 앞에 있게 된다
    arr.sort(key = lambda x : x* 3, reverse= True)
    
    return str(int("".join(arr)))
   
    return answer
print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9,33,1000]	))
print(solution([10, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([412, 41]))
# arr = [[3],[3,4],[3,1]]
# arr = sorted(arr,key=lambda x : (x[0],x[-1]))
# print(arr)