n = int(input())
t=[0]*(n+1)
p=[0]*(n+1)
dp = [0]*(n+2)
max_value = 0
for i in range(1,n+1):
    t[i],p[i] = map(int,input().split())
    # t.append(x)
    # p.append(y) 

#각 날짜부터 시작해서 끝나는 날까지의 급여
#마지막날부터 시작하면서 역행하면서 최댓값을 구해본다
for i in range(n,0,-1):
    time = t[i]+i
    if time <= n+1:
        dp[i] = max(p[i]+dp[time],max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max_value)
