N = int(input())
total = [-1 for _ in range(N+1)]
total[1] = 0
def anonymous_recur(n):
    if total[n] != -1:
        return total[n]
    if n % 3 == 0 and n % 2 == 0:
        total[n] = min(anonymous_recur(n//2), anonymous_recur(n//3)) + 1
    elif n%3==0:
        total[n] = min(anonymous_recur(n//3), anonymous_recur(n -1)) + 1
    elif n%2==0:
        total[n] = min(anonymous_recur(n//2), anonymous_recur(n -1)) + 1
    else:
        total[n] = anonymous_recur(n -1) + 1
    return total[n]

print(anonymous_recur(N))