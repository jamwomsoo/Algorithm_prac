def solution(phone_book):
    answer = True
    phone_book.sort()
    dic = {}
    for i in range(len(phone_book)-1):
        _len = len(phone_book[i])
        if _len <= len(phone_book[i+1]):
            #print(phone_book[i+1][:_len],phone_book[i])
            if phone_book[i+1][:_len] == phone_book[i]: return False
    return answer
print(solution(["119", "97674223", "1195524421"]))