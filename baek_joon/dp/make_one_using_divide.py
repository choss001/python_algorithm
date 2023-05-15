import sys
sys.setrecursionlimit(10**6)


N = int(input())
visited = {}
answer = 1e9
def recursive(n, count, source):
    global answer
    if answer < count:
        return
    if n != N:
        if (n, source) not in visited:
            visited[(n, source)] = count
        elif visited[(n, source)] > count:
            visited[(n, source)] = count
        else:
            return

    if n == 1:
        answer = min(answer, count)
        return

    if n == 0 or n < 0:
        return
    if source == 1:
        recursive(n-1, count + 1, 3)
        recursive(n-1, count + 1, 2)
        recursive(n-1, count + 1, 1)
        
    elif  n % source ==0:
        recursive(n//source, count + 1, 3)
        recursive(n//source, count + 1, 2)
        recursive(n//source, count + 1, 1)
    return

    
recursive(N, 0, 3)
recursive(N, 0, 2)
recursive(N, 0, 1)
print(answer)




n = int(input())
d = [0] * (n + 1)
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
        
print(d[n])
