# 못품
# 백준 사이트 : https://www.acmicpc.net/problem/2226
# 해설 :  https://home-body.tistory.com/m/86?category=713676

N = int(input())
cnt_0 = 0
cnt_1 = 1
for i in range(N-1):
    if i%2 == 1:
        tmp_cnt_0 = cnt_0 + cnt_1 - 1
    else:
        tmp_cnt_0 = cnt_0 + cnt_1
    tmp_cnt_1 = cnt_0 + cnt_1
    cnt_0 = tmp_cnt_0
    cnt_1 = tmp_cnt_1
print(cnt_0)