if __name__ == '__main__':
    from collections import deque

    def bfs(n, k):
        queue = deque([(n, 0)])  # start node and time
        visited = set()
        
        while queue:
            pos, time = queue.popleft()
            visited.add(pos)
            
            if pos == k:
                return time
            
            # teleport
            if pos * 2 <= 100000 and pos * 2 not in visited:
                queue.append((pos * 2, time))
                
            # walk
            if pos - 1 >= 0 and pos - 1 not in visited:
                queue.append((pos - 1, time + 1))
            if pos + 1 <= 100000 and pos + 1 not in visited:
                queue.append((pos + 1, time + 1))

    print(bfs(0, 100000))
