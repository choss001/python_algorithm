import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
visited = [False] * 200001


q = deque()
q.appendleft((n, 0))

while q:
    dn, dm = q.popleft()
    if dn == m:
        print(f'{dm}')
        break
    
    if 0 <= dn <= 100000 and visited[dn] == False:
        if 0< dn:
            q.appendleft((dn * 2, dm))
        if dn > 0 and visited[dn -1] == False:
            q.append((dn -1, dm +1))
        if visited[dn + 1] == False:   
            q.append((dn + 1, dm + 1))
    visited[dn] = True
#print(f'{visited}')
