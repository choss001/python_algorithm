if __name__ == '__main__':
    from collections import deque

    n, k = 0, 100000

    visited = [False] * 100001

    queue = deque([(n, 0)])

    while queue:
        curr, time = queue.popleft()
        visited[curr] = True

        if curr == k:
            print(time)
            break

        if curr * 2 <= 100000 and not visited[curr * 2]:
            queue.appendleft((curr * 2, time))

        if curr + 1 <= 100000 and not visited[curr + 1]:
            queue.append((curr + 1, time + 1))

        if curr - 1 >= 0 and not visited[curr - 1]:
            queue.append((curr - 1, time + 1))
