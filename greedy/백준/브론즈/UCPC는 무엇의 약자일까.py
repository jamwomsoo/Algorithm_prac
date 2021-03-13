import sys
arr = str(input())
answer = ["U","C","P","C"]

def find(array,x):
    for i in range(len(array)):
        if array[i] == x:
            return i
    return -1

for i in range(len(answer)):

    index = find(arr,answer[i])
    if index == -1:
        print("I hate UCPC")
        sys.exit()
    else:
        arr = arr[index+1:]
print("I love UCPC")