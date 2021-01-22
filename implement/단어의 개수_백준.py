import sys
input = sys.stdin.readline 
s = list(map(str, input().split()))
s = [i.upper for i in s]
print(len(s))
