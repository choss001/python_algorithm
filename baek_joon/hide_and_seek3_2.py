if __name__ == '__main__':
    from collections import deque

    def search(N):

        visited = [0] * 100001
        Q = deque()
        Q.append(N)

        while Q:
            position = Q.popleft()
            if position == K:
                return visited[position]

            for next_position in (position + 1, position - 1, position * 2) :

                if 0 <= next_position < 100001:
                    if visited[next_position] == 0:
                        if next_position == position * 2 and next_position != 0:
                            visited[next_position] = visited[position]
                            Q.appendleft(next_position)
                        else:
                            visited[next_position] = visited[position] + 1
                            Q.append(next_position)


    N, K = 5, 17
    answer = search(N)
    print(answer)
