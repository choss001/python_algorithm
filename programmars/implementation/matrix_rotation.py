def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for ta in table:
        print(ta)
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer

rows, columns, queries = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows,columns, queries))


#[1,1,4,3]
#range(2,5)
#table[1][[query[1]] = table[2][query[1]]
#table[1][1] = table[2][1]
#table[2][1] = table[3][1]
#table[3][1] = table[4][1]
range(2,4)
table[4][1] = table[4][2]
table[4][2] = table[4][3]
range(3,0,-1) 3,2,1
table[4][3] = table[3][3]
table[3][3] = table[2][3]

