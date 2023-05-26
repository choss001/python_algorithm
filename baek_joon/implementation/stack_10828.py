from collections import deque
N = int(input())

stack_list = [input() for _ in range(N)]

deq = deque()
for statement in stack_list:
    if statement.find('push') != -1:
        deq.append(statement.split()[1])
    elif statement == 'top':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[len(deq) -1])
    elif statement == 'size':
        print(len(deq))
    elif statement == 'empty':
        print(1 if len(deq) == 0 else 0)
    elif statement == 'pop':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
