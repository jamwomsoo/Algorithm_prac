#나는 못 품
#해설 학습
#현재 곳간 n을 털때 n-1 곳간을 털었으면 털 수 없음
#현재 곳간 n을 털때 n-2 곳간을 털었으면 털 수 있음
#왼쪽부터 차례대로 현재 곳간을 털때를 가정하고 최대를 만드는 방법으로, d리스트의 n번째 곳간을 털때의 최대량를 넣는다
#4(1,3,1,5) 가 있을때
#0번째 곳간을 털때 1, 1번째 곳간을 털때 3
#2번째부터는 생각을 해봐야한다, 1(0)+1(2)가 클지 3(2)이 클지 선택해본다. 2번째 곳간은 3이 최대치다
#3번째 곳간을 털때를 생각해보자. 배열 d에는 항상 해당 순서의 곳간을 털었을때의 최대치가 들어있다. 
#3번쨰 곳간을 털때는 현재최대치 = 두개 전(곳간)의 최대치 + 현재 곳간의 량, 한개전(곳간까지)의 최대치 중에서 선택 한다
#이렇게 진행 할때에 배열 d에는 항상 이전의 최대치만 들어있어서 n-3은 고려하지 않아도 된다
 
n = int(input())
arr = list(map(int,input().split()))
d=[0]*100
d[0] = arr[0]
d[1] = max(arr[0],arr[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2]+arr[i])

print(d[n-1])