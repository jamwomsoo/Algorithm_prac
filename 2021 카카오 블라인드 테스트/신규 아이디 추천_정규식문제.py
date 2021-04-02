# 정규식으로 풀어야됨
import re
def solution(new_id):
    answer = ''
    n = len(new_id)
    alnum = ['-','_','.']
    
    # 1.
    new_id = new_id.lower()
    tmp_id =''
    #print("1.",new_id)
    # 2
    new_id = re.sub('[^a-z-_.0-9]','',new_id)
    # 3
    new_id = re.sub('[.]+','.',new_id)
   
    #print(new_id)

    # 4
 
    if  new_id != '' and new_id[-1] == '.':
        new_id = new_id[:-1]
    if  new_id != '' and new_id[0] == '.':
        new_id = new_id[1:]
    #print("4.",new_id,new_id == '')
    # 5
    if new_id =='':
        new_id+='a'
    #print('5.',new_id)
    # 6
    if len(new_id)>=16:
        new_id = new_id[:15]
        #print(len(new_id))
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    #print('6.',new_id)
    # 7
    while len(new_id)<=2:
        new_id+=new_id[-1]

    return new_id
#print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
#print(solution("123_.def"))
# print(solution("abcdefghijklmn.p"))
print(solution('#.a..#'))