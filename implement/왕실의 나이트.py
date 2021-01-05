ip = input()
dic = {'a':1 , 'b':2, 'c':3, 'd':4, 'e':5, 'f':6 ,'g':7 ,'h':8}
m = int(ip[1])
n = int(dic[ip[0]])
plans=[[2,1],[-2,1],[2,-1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
x = [0,0,-1,1]
y = [-1,1,0,0] 
move = 3
cnt = 0
for plan in plans:
    xn = plan[0] + n
    yn = plan[1] + m
    if xn<1 or yn < 1 or xn>8 or yn>8:
        continue
    cnt+=1
print(cnt)

#풀이
#ord 문자를 아스키 코드 값으로 변환해주는 함수
# input_data = input()
# raw = int(input_data[1])
# column = int(ord(input_data[0]))-int(ord('a'))+1

# plans = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1))
# cnt=0
# for plan in plans:
#     next_raw = raw + plan[1]
#     next_column  = column + plan[0]
#     if next_raw >=1 and next_column >=1 and next_raw <=8 and next_column <= 8:
#         cnt+=1
# print(cnt)