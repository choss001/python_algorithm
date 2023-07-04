genres =["classic", "pop", "classic", "classic", "pop", "classic", "classic"] 
plays = [500, 600, 150, 800, 2500, 150, 150]

def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    print(f'dic1 = {dic1},\n dic2 = {dic2}')
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        print(f'k = {k}, v={v}')
        print(f'dic1[k] = {dic1[k]}, sorted = {sorted(dic1[k], key=lambda x:x[1], reverse=True)}')
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True):
            print(f'i = {i}, p = {p}')
            answer.append(i)

    return answer
print(solution(genres, plays))
