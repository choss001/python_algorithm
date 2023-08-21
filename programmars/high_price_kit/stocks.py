prices = [4,5,6,2,3,3,2,1]

def solution(prices):
    length = len(prices)
    
    # answer을 max값으로 초기화  
    answer = [ i for i in range (length - 1, -1, -1)]
    
    # 주식 가격이 떨어질 경우 찾기
    stack = [0]
    for i in range (1, length):
        print(f'stack = {stack}')
        while stack and prices[stack[-1]] > prices[i]:
            print(f'stack[-1] = {stack[-1]}, i = {i}')
            j = stack.pop()
            print(f'j = {j}')
            answer[j] = i - j
            print(f'after answer = {answer}')
        stack.append(i)
        print(f'after stack = {stack}')
    return answer

print(solution(prices))
