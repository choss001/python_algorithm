from collections import deque

def solution(bridge_length, weight, truck_weights):
    li = [0]*bridge_length
    q = deque(li)
    
    k = 0
    answer = 0
    print(f'q={q}')
    q_sum = 0
    while True:
        #print(f'q={q}, q_sum={q_sum}, k={k}, answer={answer}')
        if k == len(truck_weights):
            if q_sum == 0: break
            else: 
                q_sum -= q.pop()
                q.appendleft(0)
                answer += 1
                continue
        if truck_weights[k] + q_sum - q[-1] <= weight:
            q_sum -= q.pop()
            q.appendleft(truck_weights[k])
            q_sum += truck_weights[k]
            k+=1
        else:
            q_sum -= q.pop()
            q.appendleft(0)
        answer += 1
    return answer

bridge_length, weight, truck_weights = 2, 10, [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))
