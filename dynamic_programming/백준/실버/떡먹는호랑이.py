D,K = map(int, input().split())
dp = [None]*(D+1)
dp[0] = 'x'
dp[1] = 'y'
for i in range(2,D):
    dp[i] = dp[i-1]+dp[i-2]
x_num = dp[D-1].count('x')
y_num = dp[D-1].count('y')
i = 1
ans = []

while True:
   
    if abs(K - x_num*i) % y_num == 0:
       ans = sorted([i,abs(K - x_num*i) // y_num]) 
       break
    i+=1
for i in range(2):
    print(ans[i])