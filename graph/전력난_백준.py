while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    parent = [i for i in range(m)]
    def find_parent(parent, x):
        if parent[x] != x:
            parent[x] = find_parent(parent,parent[x])
        return parent[x]
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a< b:
            parent[b] = a
        else:
            parent[a] = b
    data = []
    for i in range(n):
        x,y,z = map(int, input().split())
        data.append([z,x,y])
    #end = map(int, input().split())
    data.sort()
    result = 0
    total = 0
    for i in data:
        v,x,y = i
        total+=v
        if find_parent(parent, x) != find_parent(parent,y):
            union_parent(parent, x, y)
            result += v
    print(total - result)
