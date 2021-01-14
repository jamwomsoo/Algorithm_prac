import bisect

n = int(input())
ls = list(map(int,input().split()))
def solution(arr,target, start,end ):
    if start> end:
        return None
    mid = (start+end) //2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return solution(arr,target,start,mid - 1)
    else:
        return solution(arr, target, mid+1,end)   
def main():
    for i in range(len(ls)):
        if i == solution(ls,i,0,len(ls)-1):
            return i
    return -1
print(main())
#print(solution(ls,ls[len(ls)//2],0,len(ls)-1)) 