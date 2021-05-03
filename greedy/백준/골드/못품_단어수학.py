# 백준 사이트 https://www.acmicpc.net/problem/1339
# 참고 사이트 https://velog.io/@sch804/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1339%EB%B2%88-%EB%8B%A8%EC%96%B4-%EC%88%98%ED%95%99
# 설명
# 알파벳이 나올때 마다 해당 알파벳을 key로 갖고 있는 dictonary에 10*(자리수)를 더해준다
# ex) ABC
# A:100 B:10 C:1
# dictionary의 사전의 value들만 빼서 정렬후 가장 큰 수부터 k(9부터 시작)해서 곱해준다
# 100*9 + 10*8 + 1*7 
n = int(input())

words = []

for i in range(n):
    words.append(str(input()))

dict = {}

for word in words:
    k = len(word) - 1
    for s in word:
        if s in dict:
            dict[s] += pow(10,k)
        else:
            dict[s] = pow(10,k)
        k-=1

nums = []


for value in dict.values():
    nums.append(value)

nums.sort(reverse=True)

ans, t = 0, 9

for i in range(len(nums)):
    ans += nums[i]*t
    t-=1

print(ans)