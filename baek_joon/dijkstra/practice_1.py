graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import sys
import heapq
input = sys.stdin.readline
def dijkstra(start):
    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (start, 0))
    while queue:
        cur_destination, cur_distance = heapq.heappop(queue)

        print(f'cur_destination = {cur_destination} , cur_distance = {cur_distance}')
        for new_destination, new_distance in graph[cur_destination].items():
            distance = cur_distance + new_distance 
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, (new_destination, distance))


    print(f'queue = {distances}')
    

dijkstra(input()[:-1])
