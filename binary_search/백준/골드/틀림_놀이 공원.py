#틀림
# 해설
# 아이들 N 명 보다 작은 숫자가 탄 t초를 구한다(t+1 초 후에는 총 n명이됨)
# t+1초에서 놀이기구를 탈때 앞에서 부터 태우고 그때부터 한명씩 추가해서 N 명이 될때의 놀이기구를 구하면됨

# 알고리즘
#1. 이분탐색 (몇초에 N명은 아니지만 제일 근접한 수 인지 구해서 시간을 return)
#2. 그 시간 + 1 초일때 놀이기구에 한명씩 태워서 n명이 됬을 때 답을 return 

def search(n,m,time_ls):
    start,end = 0, n*max(time_ls)
    max_num,max_min = 0,0
    while start<=end:
        mid = (start+end)//2
        num = sum([ (mid-1) // time + 1 for time in time_ls]) # -> 키포인트
        if num < n:
            start = mid +1
            max_num = num
            max_min = mid
        else:
            end = mid - 1

    for i,time in enumerate(time_ls):
        if max_min % time == 0:
            max_num+=1
            if max_num == n:
                return i+1



n,m = map(int, input().split())
time_ls = list(map(int, input().split()))
ans = search(n,m,time_ls)
print(ans)





























# 내 풀이
# N,M = map(int, input().split())
# arr = list(map(int, input().split()))
# def search_arr(second):
#     ride_people = M
#     for ele in arr:
#         ride_people += second//ele
#     return ride_people
# def check_last(second):
#     ls = -1
#     for ele in arr:
#         if second % ele == 0:
#             ls = max(ls,ele)
#     return ls

# def binary_search(start,end,N):
#     value = None
#     while start < end:
#         mid = (start+end)//2
#         #print(mid)
#         ride_people = search_arr(mid)
#         if ride_people > N:
#             value = mid
#             end=mid-1
#         else:
#             start=mid+1
#     return value
# ans = 0
# if N<=M:
#     print(N)
# else: 
#     t = binary_search(0,max(arr)*N,N)

#     ans = check_last(t)
#     print(ans+1)
