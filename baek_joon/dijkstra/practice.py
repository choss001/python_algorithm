graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq  

def dijkstra(graph, start):
  distances = {node: float('inf') for node in graph}  
  print(f'distance = {distances}')
  distances[start] = 0  
  queue = []
  heapq.heappush(queue, [distances[start], start])  
  print(f'first queue = {queue}')

  while queue:  
    current_distance, current_destination = heapq.heappop(queue)  

    print(f'current_distance = {current_distance}, current_destination = {current_destination}')
    print(f'distances[current_destination] = {distances[current_destination]}')
    if distances[current_destination] < current_distance:  
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      distance = current_distance + new_distance  
      print()
      print(f'before distance = {distance}, new_destination = {new_destination}, new_distance = {new_distance}')
      if distance < distances[new_destination]:  
        distances[new_destination] = distance
        print()
        print(f'go through in if statement distances[new_desticnation] = {distances[new_destination]}')
        heapq.heappush(queue, [distance, new_destination])  
    
  return distances

print(dijkstra(graph, 'C'))
