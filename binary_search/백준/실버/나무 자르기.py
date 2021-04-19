def binary_search(array,target,start,end):
    global ans
    while start<=end:
        
        mid = (start+end)//2
        #print("ans,mid",ans,mid)
        tmp = 0
        for i in arr:
            if i>mid:
                tmp+=i-mid
        #print(tmp,target)
        if target == tmp:
            ans = mid
            return
        elif target<tmp:
            start=mid+1
            ans = max(mid,ans)
        else:
            end = mid-1
            
            

n,m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
binary_search(arr,m,0,max(arr))
print(ans)