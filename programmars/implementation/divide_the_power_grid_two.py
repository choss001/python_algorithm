import sys
from collections import deque
input = sys.stdin.readline
def DFS(v, graph, visited, check_link):
    cnt = 1
    visited[v] = True
    print(f'v = {v}')
    
    for adj_v in graph[v]:
        # 방문 이력이 없고, 그 간선이 임시로 없앤 간선이 아닌 경우
        if visited[adj_v] == False and check_link[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check_link)
            
    return cnt

def solution(n, wires):
    answer = 1e9
    
    # 없앤 간선인지 아닌지 체크 값이 들어있는 리스트
    check_link = [[True]*(n+1) for _ in range(n+1)]
    
    graph = [[] for _ in range(n+1)]
    cnt_all = []
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    print(f'graph = {graph}')
    for a, b in wires:
        visited = [False]*(n+1)
        
        check_link[a][b] = False # a-b 간선 끊기
        cnt_a = DFS(a, graph, visited, check_link)
        cnt_b = DFS(b, graph, visited, check_link)
        check_link[a][b] = True # a-b 간선 다시 연결
        
        answer = min(answer, abs(cnt_a - cnt_b))
        
    return answer


wires, n = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]], 9
print(solution(n, wires))
