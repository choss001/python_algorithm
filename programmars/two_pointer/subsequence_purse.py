from sys import maxsize

INF = maxsize

sequence = [2, 3, -6, 1, 3, -1, 2, 4]
sequence = [-2, 3, 6, 1, -3, -1, -2, 4]
sequence = [2, -3, -6, -1, 3, 1, 2, -4]

def solution(sequence):
    answer = -INF
    size = len(sequence)
    s1 = s2 = 0				# 1
    s1_min = s2_min = 0		# 2
    pulse = 1
    
    for i in range(size):
        s1 += sequence[i] * pulse
        s2 += sequence[i] * (-pulse)
        print(f's1={s1},s2={s2},s1-min={s1_min},s2_min={s2_min},i={i}')
        
        # 3
        answer = max(answer, s1-s1_min, s2-s2_min)
        print(f'answer = {answer}')
        
        # 4
        s1_min = min(s1_min, s1)
        s2_min = min(s2_min, s2)
        print(f's1_min={s1_min}')
        print(f's2_min={s2_min}')
        
        # 5
        pulse *= -1
    return answer
print(solution(sequence))
