import sys
sys.setrecursionlimit(10000000)
n=int(input())


total={1:0}
def rmin(n):
    print(f'n = {n}, total = {total}')
    if n in total:
        return total[n]
    else:
        if n%3==0 and n%2==0:
            total[n]=min(rmin(n//3),rmin(n//2))
        elif n%3==0:
            total[n]=min(rmin(n-1),rmin(n//3))
        elif n%2==0:
            total[n]=min(rmin(n-1),rmin(n//2))
        else:
            total[n]=rmin(n-1)
        print(f'total[{n}] = {total[n]+1}')
        total[n]=total[n]+1
        return total[n]
print(rmin(n))
print(total)
