N, M = map(int, input().split()) 
if N == 1:
    # 못 움직임(시작한 한칸만 가능)
    result = 1
elif N < 3:
    # N이 3보다 작으면 위, 아래로는 2칸씩은 못 움직이고 한칸씩 오른쪽 두칸씩이 최선
    # 처음 위치 한 칸을 빼고 남은 칸을 2칸씩 움직이는 걸로 나누면 옆으로 총 갈 수 있는 칸수가 나오는데
    # 이때 이동 회수 3회 초과 부터는 무조건 4가지 방식을 다 사용해야 하므로 최대 4칸이여야 한다
    # 1더한건 시작칸
    result = min(4,(M-1)//2+1)
elif N >= 3 and M<7: 
    # N이 3이상이면 위, 아래로 두칸씩 가도 상관 없고
    # 오른쪽으로 한칸씩 가는게 최선
    # 하지만 이동 3회 초과부터는 4가지 방식을 다 사용해야 하므로 최대 4칸
    # 1더한건 시작칸
    result = min(4,(M-1)+1)
else: 
    # 이동 4번 이상부터 한번씩 다 써줘야됨
    # 옆으로 한칸씩 가는게 최대 이동 횟수에 좋다
    # 처음 시작 1칸, 2,3번을 통해 오른쪽으로 2칸씩이동해서 통과한 칸 수 각각 1회씩 2회
    # 2,3번으로 이동했으므로 총 남은 가로칸은 시작칸 한칸과 2씩 이동한 칸수 각각 1회 4칸을 빼준 상태에서
    # 오른쪽으로 한칸씩 이동하는게 최대 이동 
    result = 1 + 2 +(M-1-4) 
print(result)



