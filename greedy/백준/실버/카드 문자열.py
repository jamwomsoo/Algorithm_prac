for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, input().split()))
    result =''
    for i in arr:
        if result == '':
            result+=i
            continue
        if result[0] >= i:
            result = i+result
        else:
            result+=i
    print(result)