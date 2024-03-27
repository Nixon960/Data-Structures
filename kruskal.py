#GROUP ONE 

#minimum spanning tree

def kruskal(graph):
    #Sort all edges in increasing order of weight
    edges = sorted((weight, u, v) for u in graph for v, weight in graph[u])

    min_spanning_tree = []

    parent = {i: i for i in graph}

    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) 
        return parent[x]

    def union(x, y):
        parent[find(x)] = find(y)

    
    for weight, u, v in edges:
        if find(u) != find(v): 
            min_spanning_tree.append((u, v, weight))
            union(u, v)

    return min_spanning_tree


graph = {
    0: [(1, 4), (2, 8)],
    1: [(0, 4), (2, 11), (3, 8)],
    2: [(0, 8), (1, 11), (4, 7), (3, 1)],
    3: [(1, 8), (2, 1), (4, 2), (5, 6)],
    4: [(2, 7), (3, 2), (5, 4)],
    5: [(3, 6), (4, 4)]
}


print("Minimum spanning tree:")
for edge in kruskal(graph):
    print(edge)

#Odongokara Oscar 
#Kiisa Angela
#Mutumba Benjamin 
#Buwembo David Denzel 
#Nziriga Isaac Nickson