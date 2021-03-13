#어렵
for _ in range(int(input())):
    a,b = map(str,input().split())
    
    arr1 = list(a)
    arr2 = list(b)
    n = len(arr1); m = len(arr2)
    cnt = [0,0]
    diff= 0
    # 두 수가 다른 곳의 수를 세준다 == diff
    # 두 수의 1의 개수도 따로 세어준다 = cnt[0],cnt[1]
    # 만약 1의 개수가 같다면:
    # -> 다른 부분만 바꾸어주면 됨 diff//2
    # 만약 1의 개수가 틀리면:
    # -> 1. 1의 개수를 차이만큼 바꾸어준다
    # 그러면 두수가 다른 곳도 1로 채워져서 비슷해질 수 있음
    # -> 2. 그려면 1의 개수는 비슷해졌으니 1로 바꾼부분을 뺀 나머지 수에 //2해주고 1에서 바꾼부분의 개수만큼 더해주면 된다
    for i in range(n):
        if int(arr1[i]) == 1:
            cnt[0]+=1
        if int(arr2[i]) == 1:
            cnt[1]+=1
        if arr1[i] !=arr2[i]:
            diff+=1
    
    if cnt[0] == cnt[1]:
        ans = diff//2
    else:
        tmp = abs(cnt[0]-cnt[1])
        ans = (diff-tmp)//2 + tmp

    print(ans)