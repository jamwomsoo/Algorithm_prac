# 백준 저지 https://www.acmicpc.net/status?user_id=tjdtn4806&problem_id=2467&from_mine=1
# 틀림
# 투포인터를 이용
# 양 끝 점에서 start, end를 잡는다
# 두 값을 더해서 절대값이 0보다 크면 end의 인덱스를 줄이고
# 두 값을 더해서 절대값이 0보다 작으면 start의 인덱스를 늘린다
# 이때 start,end의 합의 절대값이 기존의 ans보다 작으면 바꾼다


n = int(input())
arr = list(map(int, input().split()))

arr.sort()

start = 0
end = n-1

ans = [abs(arr[start]+arr[end]),(arr[start],arr[end])]

while start< end:
    mix = arr[start] + arr[end]
    if abs(mix) < ans[0]:
        ans[0] = abs(mix)
        ans[1] = (arr[start],arr[end])
    if mix > 0:
        end -= 1
    elif mix < 0:
        start+=1
    else:
        print(*ans[1])
        exit()
print(*ans[1])
    