n,w = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 0
for i in range(n):
    #print("have money",i+1,w,'arr',arr[i])
    if i == n-1 and cnt >0:
        w += cnt*arr[i]
        cnt = 0
        break
    if i ==n-1:
        break
    if arr[i] < arr[i+1] and w>=arr[i]:
        cnt = w//arr[i]
        w = w%arr[i]
    if arr[i] > arr[i+1] and cnt>0:
        w +=cnt*arr[i]
        cnt = 0

print(w) 
