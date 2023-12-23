from collections import Counter


def solution(weights):
    answer = 0
    
    # 1:1
    counter = Counter(weights)
    print(f'counter = {counter}')
    for k,v in counter.items():
        if v>=2:
            answer+= v*(v-1)//2
    print(f'answer = {answer}')
    weights = set(weights) 
    print(f'set weights = {weights}')
    
    # 2:3 2:4 3:4 비율 가지면 짝궁 가능함
    for w in weights:
        print(f'w={w}, counter[{w}]={counter[w]}')
        if w*2/3 in weights:
            print(f'counter[w*2/3]={counter[w*2/3]}, w*2/3={w*2/3}')
            answer+= counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            print(f'counter[w*2/4]={counter[w*2/4]}, w*2/4={w*2/4}')
            answer+= counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            print(f'counter[w*3/4]={counter[w*3/4]}, w*3/4={w*3/4}')
            answer+= counter[w*3/4] * counter[w]
    return answer

weights = [100,180,360,100,270,360]
print(solution(weights))
