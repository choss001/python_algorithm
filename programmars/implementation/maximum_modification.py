from itertools import permutations

def solution(expression):
    modification = ['-','*','+']
    base_elements = list(permutations(modification,3))
    expression = expression.replace('-','|-|').replace('*','|*|').replace('+','|+|').split('|')
    print(f'expression = {expression}')

    def dfs(modification,current,result, idx, cal_idx):
        print(f'modification = {modification}')
        if cal_idx != -1:
            temp_sum = 0
            if current[cal_idx] == '-': temp_sum = int(current[cal_idx-1]) - int(current[cal_idx+1])
            if current[cal_idx] == '+': temp_sum = int(current[cal_idx-1]) + int(current[cal_idx+1])
            if current[cal_idx] == '*': temp_sum = int(current[cal_idx-1]) * int(current[cal_idx+1])
            current[cal_idx] = temp_sum
            del current[cal_idx-1]
            del current[cal_idx]
            print(f'cal current = {current}')
        if len(current) == 1:
            result[0] = max(result[0], abs(current[0]))
            return
        for i in range(idx,3):
            for k in range(len(current)):
                if modification[i] == current[k]:
                    dfs(modification, current,result, i, k)
                    return
        return
    answer = [-1]
    for modi in base_elements:
        print(f'modi={modi}')
        temp_answer = [-1]
        dfs(modi,expression.copy(),temp_answer,0,-1)
        print(f'temp_answer = {temp_answer}')
        answer[0] = max(temp_answer[0], answer[0])


    print(f'answer = {answer}')
    return answer
    
#expression = "100-200*300-500+20"
expression = "50*6-3*2"
print(f'solution = {solution(expression)}')

#   dfs(modi_sequence,current,[result], idx, cal_idx):
#       calculate current using cal_idx
#       calculate remove cal_idx front before sum mid
#       if len(current) == 1:
#           if abs result is more than befor result then set result
#           return
#       for i in range(idx,3)
#           if find modi_sequence[i]:
#               dfs(modi_sequence, current_calculated,result, idx, cal_idx)


