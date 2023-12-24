from collections import deque

def solution(queue1, queue2):
    two_v_sum = sum(queue1) + sum(queue2)
    middle_v = 0
    if two_v_sum % 2 == 1:
        return -1
    else:
        middle_v = two_v_sum//2

    solution_queue = deque([(deque(queue1), deque(queue2), 0)])
    
    while solution_queue:
        l_q, r_q, count = solution_queue.popleft()
        print(f'l_q={l_q}, r_q={r_q}, count={count}')
        if sum(l_q) == middle_v:
            return count
        if len(queue1)+ len(queue2) <count:
            break 
        if not l_q or not r_q:
            print(f'l_q={l_q}, r_q = {r_q}')
            continue
        l_q.append(r_q.popleft())
        solution_queue.append((deque(l_q), deque(r_q), count+1))
        r_q.appendleft(l_q.pop())
        r_q.append(l_q.popleft())
        solution_queue.append((deque(l_q), deque(r_q), count+1))
        

    return -1
#queue1, queue2 = [3,2,7,2],[4,6,5,1]
queue1, queue2 = [1,1],[1,5]
print(solution(queue1,queue2))


