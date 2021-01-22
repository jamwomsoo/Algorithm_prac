n= int(input())
given_point=[[0]*4 for _ in range(3)]#total, three_point, teo_point, num

for i in range(n):
    points = list(map(int,input().split()))
    for j in range(3):
        given_point[j][0]+=points[j]
        given_point[j][3] = j+1
        if points[j] == 3:
            given_point[j][1]+=1
        if points[j] ==2 :
            given_point[j][2]+=1
given_point = sorted(given_point, key = lambda x: (-x[0],-x[1],-x[2]))
tmp = [given_point[i][:3] for i in range(len(given_point))]

if tmp.count(tmp[0]) >=2:
    print(0,given_point[0][0])
else:
    print(f'{given_point[0][3]} {given_point[0][0]}')
