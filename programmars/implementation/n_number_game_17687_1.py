big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
            print(f'b = {b}')
        a=a+b
        print(f'a={a}')
        i=i+1
        print(f'i, j = {i}, {j}')
    answer = a[p-1::m][:t]
    return answer

n,t,m,p = 16,16,2,1
print(solution(n,t,m,p))
