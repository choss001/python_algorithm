from typing import Tuple, Set
import copy

def get_pos(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                r_pos = (i, j)
            elif maze[i][j] == 2:
                b_pos = (i, j)
            elif maze[i][j] == 3:
                r_target_pos = (i, j)
            elif maze[i][j] == 4:
                b_target_pos = (i, j)
            else:
                pass
    return r_pos, b_pos, r_target_pos, b_target_pos

def solution(maze):
    global answer 
    answer = 2^32
    r_visited = list()
    b_visited = list()
    r_pos, b_pos, r_target_pos, b_target_pos = get_pos(maze)
    lx = len(maze)
    ly = len(maze[0])
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    
    # dfs의 역할
    # 전달 받은 위치에 대하여 방문처리 + 상하좌우 방향으로 다음 칸 전달(4번 호출)
    # r_maze, b_maze 에서 각 수레가 한칸씩 움직인다
    
    def dfs(r_pos: Tuple[int, int], b_pos: Tuple[int, int], r_visited: Set[Tuple[int, int]], b_visited: Set[Tuple[int, int]], depth):
        global answer
        # 종료 조건
        # 둘 다 타겟에 도달한 경우
        if r_pos == r_target_pos and b_pos == b_target_pos:
            if depth < answer:
                answer = depth
            return
        
        # 방문 처리
        r_visited.append(r_pos)
        b_visited.append(b_pos)
        print(f'r_visited = {r_visited}, b_visited = {b_visited}')
        
        # 다음 이동. 다음과 같은 제한사항 주의
        # 0. 벽이 아니어야함
        # 1. 수레는 벽이나 격자 판 밖으로 움직일 수 없습니다.
        # 2. 수레는 자신이 방문했던 칸으로 움직일 수 없습니다.
        # 3. 자신의 도착 칸에 위치한 수레는 움직이지 않습니다. 계속 해당 칸에 고정해 놓아야 합니다.
        # 4. 동시에 두 수레를 같은 칸으로 움직일 수 없습니다.
        # 5. 수레끼리 자리를 바꾸며 움직일 수 없습니다.
        for dx1, dy1 in dir:
            if r_pos == r_target_pos: # 조건 3
                n_r_pos = r_pos
                print(f'r_pos == r_target_pos = {n_r_pos}')
            else:
                n_r_pos = (r_pos[0] + dx1, r_pos[1] + dy1)
                print(f'not ! r_pos == r_target_pos = {n_r_pos}')
            # 조건 1, 0, 2
            if (0 > n_r_pos[0] or n_r_pos[0] >= lx  or 0 > n_r_pos[1] or n_r_pos[1] >= ly) \
                or (maze[n_r_pos[0]][n_r_pos[1]] == 5)\
                or (n_r_pos in r_visited and n_r_pos != r_target_pos):
                continue
            for dx2, dy2 in dir:
                if b_pos == b_target_pos:
                    n_b_pos = b_pos
                else:
                    n_b_pos = (b_pos[0] + dx2, b_pos[1] + dy2)
                # 조건 1, 0, 2, 4, 5
                if (0 > n_b_pos[0] or n_b_pos[0] >= lx  or 0 > n_b_pos[1] or n_b_pos[1] >= ly) \
                    or  (maze[n_b_pos[0]][n_b_pos[1]] == 5)\
                    or (n_b_pos in b_visited and n_b_pos != b_target_pos) \
                    or (n_r_pos == n_b_pos) \
                    or (n_r_pos == b_pos and n_b_pos == r_pos):
                    continue
                dfs(n_r_pos, n_b_pos, r_visited, b_visited, depth + 1)
                
        r_visited.pop()
        b_visited.pop()
    dfs(r_pos, b_pos, r_visited, b_visited, 0)
    
    if answer == 2^32:
        answer = 0
    return answer

maze = [[1, 4], [0, 0], [2, 3]]
print(solution(maze))

