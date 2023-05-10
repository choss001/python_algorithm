from collections import deque

#https://school.programmers.co.kr/learn/courses/30/lessons/60062/solution_groups?language=python3

def solution(n, weak, dist):
    dist.sort(reverse=True)
    q = deque([weak])
    print(f'q = {q}')
    visited = set()
    visited.add(tuple(weak))
    for i in range(len(dist)):
        d = dist[i]
        print(f'd = {d}')
        for _ in range(len(q)):
            print()
            current = q.popleft()
            print(f'q = {q}')
            print(f'current = {current}')
            for p in current:
                l = p
                r = (p + d) % n
                print(f' l = {l}, r = {r}')
#                if l < r:
#                    temp = tuple(filter(lambda x: x < l or x > r, current))
#                else:
#                    temp = tuple(filter(lambda x: x < l and x > r, current))
                temp = tuple(filter(lambda x: (x < l or x > r) if l < r else (x < l and x > r), current))
                print(f'temp = {temp}, visited = {visited}')


                if len(temp) == 0:
                    return (i + 1)
                elif temp not in visited:
                    visited.add(temp)
                    q.append(list(temp))

    return -1

n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]
print(solution(n, weak, dist))
