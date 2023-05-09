MAX = int(1e4) + 5
id = [i for i in range(MAX)]
p = []

def root(x):
    global id
    while id[x] != x:
        id[x] = id[id[x]]
        x = id[x]
    return x

def union1(x, y):
    global id
    p = root(x)
    q = root(y)
    id[p] = id[q]

def kruskal(p):
    minimumCost = 0
    for i in range(edges):
        x = p[i][1][0]
        y = p[i][1][1]
        cost = p[i][0]
        if root(x) != root(y):
            minimumCost += cost
            union1(x, y)
    return minimumCost

nodes, edges = map(int, input("Enter Nodes and edges: ").split())

for i in range(edges):
    print("Enter the value of X, Y, and weight:")
    x, y, weight = map(int, input().split())
    p.append((weight, (x, y)))

p.sort()
minimumCost = kruskal(p)

print("Minimum cost is", minimumCost)
