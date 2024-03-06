def solution(p):

    def get_correct_parenthesis(s):
        temp_lst = []
        temp_answer = False
        for i in range(len(s)):
            if s[i] == '(': temp_lst.append(s[i])
            elif temp_lst: temp_lst.pop()
            else: return False
        if temp_lst: return False
        return True

    
    def dfs(p):
        l,r = 0,0
        divide = 0
        for i in range(len(p)):
            if p[i] == '(': l+=1
            if p[i] == ')': r+=1
            if l != 0 and l == r:
                divide = i
                break
        u = p[:divide+1]
        v = p[divide+1:]
        if get_correct_parenthesis(u):
            if v: return u + dfs(v)
            else: return u
        temp = dfs(v)
        reverse_u = ''
        for i in range(1,len(u)-1):
            if u[i] == '(': reverse_u += ')'
            else: reverse_u += '('
        return '(' + temp + ')' + reverse_u
    return dfs(p)

#p = "((()))((()))"
#p = "()))((()"
p = ")))((("
print(solution(p))


#dfs(p,u,v):
#    u, v divide
#    u is correct and v is empty:
#        return u
#    u is correct and v is not empty:
#        return u + dfs(p,u,v,answer)
#    u is not correct:
#        return '('+dfs(p,u,v,answer)+')'+ delete first and end from u + reverse parenthesis rest of u




