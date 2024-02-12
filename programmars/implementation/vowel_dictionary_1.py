from itertools import permutations

def solution(word):


    def dfs(current, result, idx, elements):

        if current[-1] == ' ' or len(current) == 6:
            result.append(current.copy())
            return

        for i in elements:
            current.append(i)
            dfs(current, result, idx, elements)
            current.pop()


        return -1


    elements = [' ','A','E','I','O','U']
    result = []
    dfs([], result, 0, elements)
    print(f'result = {result}')
    return

#word = "AAAAE"
word = "I"

print(solution(word))

#A,AA,AAA,AAAA,AAAAA,AAAAE,AAAAI,AAAAO,AAAAU,
#AAAE,AAAEA,AAAEE,AAAEI,AAAEO,AAAEU,
#AAAI,AAAIA,AAAIE,AAAII,AAA

pseudo code


    
