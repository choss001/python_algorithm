import heapq
import sys

class Graph():
    def __init__(self):
        self.ver_dict = {}
    def add_vertex(self, vertex):
        self.ver_dict[vertex] = Vertex(vertex)
    def get_vertex(self, vertex):
        return self.ver_dict[vertex]

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.ver_dict:
            self.add_vertex(frm)
        if to not in self.ver_dict:
            self.add_vertex(to)
        self.ver_dict[frm].add_neighbor(self.ver_dict[to], cost)

    def __iter__(self):
        return iter(self.ver_dict.values())

class Vertex():

    def __init__(self, vertex):
        self.id = vertex
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None


    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight
                    

    def __str__(self):
        temp = ''
        for i in self.adjacent.keys():
            temp += str(i.id) +','
        return 'my id : '+str(self.id)+', neighbor : '+ temp

    def __str__(self):
        neighbors = ','.join(str(i.id) for i in self.adjacent.keys())
        distance = ','.join(str(i) for i in self.adjacent.values())
        return f'my id: {self.id}, mydistance : {self.distance} neighbors: {neighbors} distance : {distance}'

    def __lt__(self, other):
        self.distance < other.distance


def shortest(v, path):
    if v.previous:
        path.append(v.previous.id)
        shortest(v.previous, path)
    return


def dijkstra(aGraph, start):
    start.distance = 0
    unvisited_queue = [(v.distance ,v) for v in aGraph]

    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.visited = True

        for next in current.adjacent:
            if next.visited:
                continue
            new_dist = current.distance + current.adjacent[next]

            if new_dist < next.distance:
                next.distance = new_dist
                next.previous = current

        while(len(unvisited_queue)):
                heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.distance,v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)

v, e= map(int, input().split())
start_vertex = int(input())
input_list = [list(map(int, input().split())) for _ in range(e)]
        

g = Graph()

for i in range(1, v + 1):
    g.add_vertex(i)

for el in input_list:
    g.add_edge(el[0], el[1], el[2])

dijkstra(g, g.get_vertex(start_vertex))
for i in range(1,v+1):
    path = [g.get_vertex(i).id]
    shortest(g.get_vertex(i),path)
    if g.get_vertex(i).distance == sys.maxsize:
        print('INF')
    else:
        print(g.get_vertex(i).distance)

