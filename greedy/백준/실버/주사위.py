# https://www.acmicpc.net/problem/1041
n = int(input())
arr = list(map(int, input().split()))
 
if n== 1:
    print(sum(arr)-max(arr))
else:
    # 마주보고 있는 것들의 최소 값만 남겨서 조합의 경우의 수를 줄인다
    arr[0] =arr[5] = min(arr[5],arr[0])
    arr[1] =arr[4] = min(arr[1],arr[4])
    arr[2] =arr[3] = min(arr[2],arr[3])
    # 세 면이 모여있는 하나의 모서리 부분
    three = arr[0]+arr[1]+arr[2]
    # 두면이 모여있는 하나의 모서리 부분
    two = min(arr[0]+arr[1],arr[0]+arr[2],arr[1]+arr[2])
    one = min(arr)
    n3=4
    n2= (max(4*(n-2),0)+max(4*(n-1),0))
    n1 = (max((n-2)*(n-2),0) + max((n-2)*(n-1)*4,0)) 
    result = three*n3 + two*n2 + one*n1
 
    print(result)