from itertools import permutations

def solution(word):
    base_lst = [' ','A','E','I','O','U']
    temp_lst = list(permutations(base_lst,5))

    answer = 1
    for i in ['A','E','I','O','U']:
        for j in [' ','A','E','I','O','U']:
            if j == ' ':
                if i == word:
                    return answer
                print(f'{i} = {answer}')
                answer += 1
                continue
            for k in [' ','A','E','I','O','U']:
                if k == ' ':
                    if i+j == word:
                        return answer
                    print(f'{i+j} = {answer}')
                    answer += 1
                    continue
                for l in [' ','A','E','I','O','U']:
                    if l == ' ':
                        if i+j+k == word:
                            return answer
                        print(f'{i+j+k} = {answer}')
                        answer += 1
                        continue
                    for m in [' ','A','E','I','O','U']:
                        if m == ' ':
                            if i+j+k+l == word:
                                return answer
                            print(f'{i+j+k+l} = {answer}')
                            answer += 1
                            continue
                        if i+j+k+l+m == word:
                            return answer
                        print(f'{i+j+k+l+m} = {answer}')
                        answer += 1
    return

#word = "AAAAE"
word = "I"

print(solution(word))

#A,AA,AAA,AAAA,AAAAA,AAAAE,AAAAI,AAAAO,AAAAU,
#AAAE,AAAEA,AAAEE,AAAEI,AAAEO,AAAEU,
#AAAI,AAAIA,AAAIE,AAAII,AAA
