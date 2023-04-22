if __name__ == '__main__':
    from collections import deque

    def search(N):

        visited = [0] * 100001
        Q = deque()
        Q.append((N, [N]))

        while Q:
            (position, trace_array) = Q.popleft()
            if position == K:
                print(trace_array)
                return visited[position]

            for next_position in (position + 1, position - 1, position * 2) :

                if 0 <= next_position < 100001:
                    if visited[next_position] == 0:
                        if next_position == position * 2 and next_position != 0:
                            visited[next_position] = visited[position]
                            Q.appendleft((next_position, [*trace_array, next_position] ))
                        else:
                            visited[next_position] = visited[position] + 1
                            Q.append((next_position, [*trace_array, next_position] ))


    N, K = 0, 100000
    answer = search(N)
    print(answer)
