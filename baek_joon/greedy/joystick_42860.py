import sys
input = sys.stdin.readline

def solution(name):
    dics = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':12,'P':11,'Q':10,'R':9,'S':8,'T':7,'U':6,'V':5,'W':4,'X':3,'Y':2,'Z':1 }
    f, e = 1, len(name)-1
    direction = -1 
    while True:
        if name[f] != 'A':
            direction = 1
            break
        elif name[e] != 'A':
            direction = 0
            break
        f += 1
        e -= 1

    if direction == -1:
        return 0
    answer = dics[name[0]]
    
    if direction == 1:
        start = 1
        while start < len(name):
            answer += dics[name[start]]
            start += 1
        #move count
        move_count = 0
        for i in range(len(name) -1, 0, -1):
            if name[i] != 'A':
                move_count = i
                break
            
    elif direction == 0:
        start = len(name) -1
        while start > 0:
            answer += dics[name[start]]
            start -= 1
        #move count
        move_count = 0
        for i in range(1, len(name)):
            if name[i] != 'A':
                move_count = len(name) - i
                break
        
    
    return answer + move_count
#name = 'JEROEN'
name = 'JAN'

print(solution(name))
