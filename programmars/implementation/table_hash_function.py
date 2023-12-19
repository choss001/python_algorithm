def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x:(x[col-1],-x[0]))
    data[row_begin-1]
    answer = 0
    for i in range(row_begin-1, row_end):
        temp_sum = 0
        for k in data[i]:
            temp_sum +=k%(i+1)
        if row_begin-1 == i:
            answer = temp_sum
        else:
            answer^=temp_sum
        


    return answer
data= [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
result = 4
print(solution(data,col,row_begin,row_end))

