# 백준 택베 문제 : https://www.acmicpc.net/problem/8980
# 풀이 싸이트 : https://jjangsungwon.tistory.com/114(코드)
#       내용 : https://steadev.tistory.com/15
# 1.도착 마을을 순서대로 정렬한다
# 2.정렬된 배열을 순서대로 진행
# 2-1.해당 인덱스의 출발 마을과 도착마을 사이의 트럭잔여 용량의 최소값을 구한다
# 2-2. 2-1에의 최소갑과 현재 옮기는 박스 수를 비교해서 더 작은 것을 옮긴다
# 출발지부터 도착지까지 각 마을에서의 박스 잔여량을 줄여준다
n,c = map(int ,input().split())
m = int(input())
arr = []
for i in range(m):
    send,receive,box = map(int ,input().split())
    arr.append([send,receive,box])
arr.sort(key = lambda x: x[1])

remain = [c] * (n+1)
answer = 0

for i in range(m):
    temp = c
    for j in range(arr[i][0],arr[i][1]):
        temp = min(temp,remain[j])
    temp = min(temp,arr[i][2])
    for j in range(arr[i][0],arr[i][1]):
        remain[j] -= temp
    print(arr[i],temp)
    answer += temp

print(answer)