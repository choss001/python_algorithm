def solution(arr):
    def check(temp_lst):
        temp_value = temp_lst[0][0]
        for item in temp_lst:
            for i in item:
                if temp_value != i: return (False,temp_value)
        return (True,temp_value)
    def dfs(arr,dic):

        temp_value = check(arr)
        if temp_value[0]:
            dic[temp_value[1]] +=1
            return
        if len(arr) == 1:
            dic[arr[0][0]] += 1
            return
        length = len(arr)
        half = length//2
        base_condition = [[0,half,0,half],[0,half,half,length],[half,length,0,half],[half,length,half,length]]
        for k in range(4):
            temp_lst = []
            for i in range(half): temp_lst.append(arr[base_condition[k][0]:base_condition[k][1]][i][base_condition[k][2]:base_condition[k][3]])
            dfs(temp_lst,dic)
    dic = {0:0,1:0}
    dfs(arr,dic)
    return [dic[0],dic[1]]


#arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
#arr = [[1,1],[1,1]]
print(solution(arr))

