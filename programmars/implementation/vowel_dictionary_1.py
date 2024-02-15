from itertools import permutations
real_answer = 0
def solution(word):


    def dfs(current, result, idx, elements,answer, word):
#       temp_current = ''.join(current[:-1]) if current[-1] == ' ' else ''.join(current)
#       if (''.join(current[:-1]) if current[-1] == ' ' else ''.join(current)) == word:
#           return 

        if current:
            if current[-1] == ' ' or len(current) == 5:
                answer += 1
                #print(f"|{''.join(current)}|")
                temp_current = ''.join(current[:-1]) if current[-1] == ' ' else ''.join(current)
                #print(f'temp = {temp_current}')
                if temp_current == word:
                    #print(f'curent = {current}, word = {word}')
                    print(f'answer = {answer}')
                    return answer
                return answer

        for i in elements:
            current.append(i)
            answer = dfs(current, result, idx, elements,answer, word)
            current.pop()


        return answer

    elements = [' ','A','E','I','O','U']
    result = []
    return dfs([], result, 0, elements, 0, word)

#word = "AAAAE"
word = "I"

print(solution(word))

#A,AA,AAA,AAAA,AAAAA,AAAAE,AAAAI,AAAAO,AAAAU,
#AAAE,AAAEA,AAAEE,AAAEI,AAAEO,AAAEU,
#AAAI,AAAIA,AAAIE,AAAII,AAA



    
