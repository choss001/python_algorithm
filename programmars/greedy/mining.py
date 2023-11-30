import math

temp_lst = []
material_dic ={"diamond":25,"iron":5,"stone":1}
chart_base={"diamond":0,"iron":1,"stone":2}
def prepare(minerals):
    length = min(sum(picks)*5, len(minerals))
    for i in range(math.ceil(length/5)):
        temp_sum = 0
        for k in range(5):
            if i*5+k >= length:
                break
            temp_sum += material_dic[minerals[i*5+k]]
        
        temp_lst.append((temp_sum, i))

def stamina_check(material, pick):
    chart =[[1,1,1],
            [5,1,1],
            [25,5,1]]
    print(f'material={material}, pick={pick}, staminacheck')
    return chart[chart_base[pick]][chart_base[material]]


def solution(picks, minerals):
    length = min(sum(picks)*5, len(minerals))
    prepare(minerals)
    temp_lst.sort(reverse=True)
    dic ={}
    d,i,s = picks
    for item in temp_lst:
        if d>0:
            d-=1
            dic[item[1]] = 'diamond'
        elif i>0:
            i-=1
            dic[item[1]] = 'iron'
        elif s>0:
            s-=1
            dic[item[1]] = 'stone'
            
    answer = 0
    for i in range(length):
        pick = dic[i//5]
        answer += stamina_check(minerals[i], pick)

    return answer
#picks = [1,3,2]
picks = [0,1,1]
#minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(f'answer = {solution(picks, minerals)}')
print(f'temp_lst={temp_lst}')


