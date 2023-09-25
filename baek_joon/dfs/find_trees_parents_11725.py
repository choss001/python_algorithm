import sys
sys.setrecursionlimit(10**6)
# 테스트용 파일("input.txt") 읽기
# sys.stdin = open("input.txt", "r")

# 주어진 파일을 한 줄씩 입력
# input = sys.stdin.readline

# N 입력
N = int(input())

# tree, parent 초기화
tree = [[] for _ in range(N + 1)]
parent = [None for _ in range(N + 1)]

# DFS 정의
def DFS(graph, vertex, visited):
    for i in graph[vertex]:
        # 만약 방문하지 않았을 경우 방문할 정점의 값을 할당하고 재귀함수 호출
        if not visited[i]:
            visited[i] = vertex
            DFS(graph, i, visited)

# 주어진 노드로 트리 값 할당
for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

print(f'item = {tree}')
# DFS 함수 사용하여 parent 값 할당
DFS(tree, 1, parent)

# 각 노드의 부모 노드 번호를 2번부터 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])
