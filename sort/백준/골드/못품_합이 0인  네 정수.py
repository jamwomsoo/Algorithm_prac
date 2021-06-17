# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/7453
# 풀이 사이트 : https://jjangsungwon.tistory.com/112

# 해설:
# 배열 a 와 배열 b의 원소 각각을 더해서 나올 수 있는 수를 딕셔너리 담는다
# 배열 c 와 배열 d의 원소 각각을 더한 값 중 -를 붙인 값이 딕셔너리 key 값으로 존재한다면 경우의 수(답)를 증가시킨다.

# 알고리즘
# 1. 이중포문으로 배열 a와 배열 b의 원소를 더해 만들 수 있는 값을 dictionary의 키값으로 만들어주고 value에 나온 갯수를 작성
# 2. 이중포문으로 배열 c와 배열 d의 원소를 더한 값의 -값이 dictionary에 있으면 해당 key 값의 value값을 더해준다.
N = int(input())
arr_a = []
arr_b = []
arr_c = []
arr_d = []
dic_a_b = {}
for i in range(N):
    a,b,c,d = map(int, input().split())
    arr_a.append(a)
    arr_b.append(b)
    arr_c.append(c)
    arr_d.append(d)

# arr_a.sort()
# arr_b.sort()
# arr_c.sort()
# arr_d.sort()

for a in range(N):
    for b in range(N):
        if arr_a[a]+arr_b[b] not in dic_a_b.keys():
            dic_a_b[arr_a[a]+arr_b[b]] = 1
        else:
            dic_a_b[arr_a[a]+arr_b[b]]+=1

ans = 0
for c in range(N):
    for d in range(N):
        if -(arr_c[c]+arr_d[d]) in dic_a_b.keys(): 
            ans+=dic_a_b[-(arr_c[c]+arr_d[d])]
print(ans)