from itertools import permutations
real_answer = 0
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer

word = "I"
print(solution(word))

#A,AA,AAA,AAAA,AAAAA,AAAAE,AAAAI,AAAAO,AAAAU,
#AAAE,AAAEA,AAAEE,AAAEI,AAAEO,AAAEU,
#AAAI,AAAIA,AAAIE,AAAII,AAA



    
