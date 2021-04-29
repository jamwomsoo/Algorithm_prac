# 기존의 내방식 
# -> 앞에서부터 해당 알파벳의 숫자가 적으면 추가
# 정답
# -> 뒤에서 역으로 시작해 하나씩 제거하고 origin과 changed의 길이가 같아지면 중지 
origin = str(input())
changed = str(input())
def add_A(x):
    return x+'A'
def reverse_add_b(x):
    x = x[::-1]
    return x+'B'

while True:
    if len(origin) == len(changed):
        if origin == changed:
            print(1)
        else:
            print(0)
        break
    tmp = changed[-1]
    changed = changed[:-1]
    if tmp == 'B':
        changed = changed[::-1]

