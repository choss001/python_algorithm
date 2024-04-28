import sys
from collections import deque
input = sys.stdin.readline
def DFS(graph, n,visited, v, check_link):
    q = deque([(v,v)])
    visited[v] = True
    count = 1

    while q:
        b_v, a_v = q.popleft()
        visited[a_v] = True
        for i in graph[a_v]:
            if not visited[i] and check_link[a_v][i]:
                print(f'b_v={b_v}, a_v ={a_v}, i={i}')
                q.append((a_v,i))
                count +=1
    return count

def solution(n, wires):

    graph = [[]  for i in range(n+1)]

    for i in wires:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)
    check_link = [[True for _ in range(n+1)] for _ in range(n+1)]
    print(f'graph = {graph}')
    answer = 9999999
    for a, b in wires:
        visited = [False for i in range(n+1)] 
        check_link[a][b] = False
        check_link[b][a] = False
        a_cnt = DFS(graph,n,visited,a,check_link)
        b_cnt = DFS(graph,n,visited,b,check_link)
        print(f'a_cnt, b_cnt = {a_cnt, b_cnt}, a,b = {a,b}')
        check_link[a][b] = True
        check_link[b][a] = True
        answer = min(answer, abs(a_cnt - b_cnt))
    print(f'answer = {answer}')
    
    return answer


#wires, n = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]], 9
#wires, n = [[1,2],[2,3],[3,4]], 4
wires, n = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]], 7
print(solution(n, wires))
