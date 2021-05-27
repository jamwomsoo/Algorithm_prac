# 맞음 but 개 병맛 문제
import heapq
while True:
    try:
        X = int(input())*(10**7)

        n = int(input()) # 레고조각의 수
        rego = [int(input()) for _ in range(n)]
        rego.sort()
        l = 0
        r = n-1
        ans = []
        if n <2:
            print('danger')
            continue
        while l<r:
            if rego[l]+rego[r] == X:
                #ans.append([abs(rego[r]-rego[l]),rego[l],rego[r]])
                heapq.heappush(ans,[-abs(rego[r]-rego[l]),rego[l],rego[r]])
                
                r-=1
            elif rego[l] + rego[r] > X:
                r-=1
            else:
                l+=1
        if ans:
            print("yes {0} {1}".format(ans[0][1],ans[0][2]))
        else:
            print('danger')
    except:
        break