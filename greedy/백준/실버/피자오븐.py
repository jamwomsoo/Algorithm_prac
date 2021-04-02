# 1. 60분이 넘는 시간은 60분 타이머 버튼을 최대한 눌러 남은 시간이 60분 미만이 되도록 만듭니다.
# 2. 남은 시간이 n이라고 할 때, n이 35분 이하라면 0분에서부터 최소 횟수의 버튼을 누르고, 35분 초과라면 60분 타이머를 한번 누르고 60-n분에서 최소 횟수의 버튼을 누르는 경우를 찾는다
# 3. 만약 남은 시간 n의 일의 자리 수를 n1이라고 할 때 5이하면 1분 타이머를 n1회 누르는 것이, 5초과일 때 10분 타이머를 1회 누르고 -1 분 타이머를 (10-n1)회 누르는 것이 최소 횟수의 버튼을 누르는 경우이다
 
for _ in range(int(input())):
    n = int(input())
    count = [0,0,0,0,0]
    count[0] += n//60
    n = n%60
    def get_count(n):
        count = [0,0,0] # 10,1,-1
        count[0] +=n//10
        if n%10<=5: count[1]+=n%10
        else:
            count[0]+=1
            count[2] += 10 - n%10
        return count
    if n<=35:
        ret = get_count(n)
        count[1]+=ret[0]
        count[3]+=ret[1]
        count[4]+=ret[2]
    else:
        ret = get_count(60-n)
        count[0]+=1
        count[2] += ret[0]
        count[3] += ret[2]
        count[4] += ret[1]

    print(*count)