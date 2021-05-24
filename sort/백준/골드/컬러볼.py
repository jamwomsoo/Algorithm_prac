from collections import defaultdict
# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/10800
# 풀이 사이트 :https://jjangsungwon.tistory.com/123
# 해설
# 크기로 배열을 정렬
# 정렬된 배열의 인덱스 전까지 총무게 total과 정렬된 배열 인덱스의 전까지 해당 색상들의 총무게 color_dic을 뺴준다
# total - color_dic[index]
n = int(input())
arr = []
color_dic = defaultdict(int)
for i in range(n):
    a,b = map(int,input().split())
    arr.append([a,b,i])
    
arr=sorted(arr,key = lambda x : x[1])
ans = defaultdict(int)
total = 0
j = 0
for i in range(n):
    while arr[j][1] < arr[i][1]:
        total+=arr[j][1]
        color_dic[arr[j][0]] += arr[j][1]
        j+=1
    ans[arr[i][2]] = total - color_dic[arr[i][0]] 
for i in range(n):
    print(ans[i])

