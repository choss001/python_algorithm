def solution(rows, columns, queries):
    
    answer = []
    n = 1
    base_lst = []
    for i in range(rows):
        temp_lst = []
        for j in range(columns):
            temp_lst.append(n)
            n += 1
        base_lst.append(temp_lst)    
    (2,2), (5,4)

    for query in queries:
        answer.append(rotate(query, base_lst))

    return answer

def rotate(query, base_lst):
    min_value = 99999999
    for i in range(len(query)):
        query[i] -= 1

    temp_ru = base_lst[query[0]][query[3]]
    for i in range(query[3],query[1], -1):
        base_lst[query[0]][i] = base_lst[query[0]][i-1] 
        min_value = min(base_lst[query[0]][i], min_value)
    temp_rd = base_lst[query[2]][query[3]]

    for i in range(query[2],query[0], -1):
        base_lst[i][query[3]] = base_lst[i-1][query[3]]
        min_value = min(base_lst[i][query[3]], min_value)
    base_lst[query[0]+1][query[3]] = temp_ru
    temp_ld = base_lst[query[2]][query[1]]

    for i in range(query[1],query[3]):
        base_lst[query[2]][i] = base_lst[query[2]][i+1]
        min_value = min(base_lst[query[2]][i], min_value)
    base_lst[query[2]][query[3]-1] = temp_rd

    for i in range(query[0],query[2]):
        base_lst[i][query[1]] = base_lst[i+1][query[1]]
        min_value = min(base_lst[i][query[1]], min_value)
    base_lst[query[2]-1][query[1]] = temp_ld

    min_value = min(min_value,temp_ru)
    min_value = min(min_value,temp_rd)
    min_value = min(min_value,temp_ld)

    return min_value

#rows,columns,queries=6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
#rows,columns,queries=3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
rows,columns,queries=2,2,[[1,1,2,2]]
print(solution(rows, columns, queries))



