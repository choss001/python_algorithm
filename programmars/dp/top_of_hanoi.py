def solution(n):
    answer = []
    
    def hanoi(src, tgt, inter, n): 
        print(f'src={src}, tgt={tgt}, inter={inter}, n={n}')
        if n == 1:
            answer.append([src, tgt])
            print(f'answer = {answer}')
        else:
            hanoi(src,inter,tgt,n-1)
            hanoi(src,tgt,inter,1)
            hanoi(inter,tgt,src,n-1)
            
    hanoi(1,3,2,n)
    
    return answer

n = 3
print(f'{solution(n)}')
