import sys
n,k = map(int, input().split())
arr = list(map(int, input().split()))
state = [0]*n*2
time = 1
cnt = 0
def rotate_belt():
    global arr,state
    
    arr = arr[-1:] + arr[:-1]
    state = state[-1:] + state[:-1]
  
def move_robot():
    global arr,cnt,state,time,n
    if state.count(0) >= 2*n:
        return
    for i in range(n-1,-1,-1):
        if i == n-1 and state[i] == 1:
            state[i] = 0
        else:
            # 앞 벨트 비어있고, 내구도가 남았을때 이동
            if state[i+1] == 0 and arr[i+1] > 0 and state[i] == 1:
                state[i] = 0
                state[i+1] = 1
                arr[i+1]-=1
                if state[n-1] == 1:
                    state[n-1] = 0
                # if arr[i+1] == 0:
                #     cnt+=1
                #     if cnt>=k:
                #         print(time)
                #         sys.exit()
    

             
while True:
    # 벨트 한칸 회전
    rotate_belt()
    # 로봇 이동
    move_robot()
    # 로봇 올라가기
    if arr[0] > 0 and state[0] == 0:
        state[0] = 1
        arr[0]-=1
    # 내구도 체크
    if arr.count(0)>=k:
        break
   
    time+=1
print(time)