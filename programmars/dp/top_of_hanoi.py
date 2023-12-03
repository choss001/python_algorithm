def solution(n):
    answer = []
    
    def hanoi(src, tgt, inter, n, k): 
        print(f'src={src}, tgt={tgt}, inter={inter}, n={n}, k={k}')
        if n == 1:
            answer.append([src, tgt])
            print(f'answer = {answer}')
        else:
            print(f'hanoi 1 : ', end = '')
            hanoi(src,inter,tgt,n-1, k+1)
            print(f'hanoi 2 : ', end = '')
            hanoi(src,tgt,inter,1, k)
            print(f'hanoi 3 : ', end = '')
            hanoi(inter,tgt,src,n-1, k)
            
    hanoi(1,3,2,n,1)
    
    return answer

n = 3
print(f'{solution(n)}')
