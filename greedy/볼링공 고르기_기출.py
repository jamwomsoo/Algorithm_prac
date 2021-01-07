from itertools import combinations
#내 정답
n, m = list(map(int, input().split()))
ls = list(map(int, input().split()))
# cnt=0
# per =list( combinations(ls,2))
# for a,b in per:
#   if a != b:
#     cnt+=1

# print(cnt)
#해설
#각 볼링공 무게 별로 갯수를 샌다
#최저 무게 부터 최대 무게까지 경우의 전체 숫자에서 자신의 갯수를 뺀 나머지와 자신의 볼링 공 갯수를 구해서 더한다
#뒤로 갈수록 한 번 사용되는 경우의 수는 사라지기 때문에 경우의 수는 점점 줄어든다
arr = [0] * (m+1)
for i in ls:
  #print(i)
  arr[i] += 1
cnt = sum(arr)
result = 0
for i in range(1,m+1):
  cnt-=arr[i]
  result += arr[i]*cnt
print(result)

