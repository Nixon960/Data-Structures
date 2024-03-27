
#GROUP ONE
def dijkstra(graph, start):
    
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    
    visited = set()
    
    while len(visited) < len(graph):
        
        min_node = None
        min_distance = float('infinity')
        for node, distance in distances.items():
            if node not in visited and distance < min_distance:
                min_node = node
                min_distance = distance
        
        visited.add(min_node)
        
        
        for neighbor, weight in graph[min_node].items():
            distance = distances[min_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
    
    return distances


graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print("Shortest distances from node", start_node, ":", dijkstra(graph, start_node))

#Odongokara Oscar 
#Kiisa Angela
#Mutumba Benjamin 
#Buwembo David Denzel 
#Nziriga Isaac Nickson