from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(land):

    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]

    y_dic = defaultdict(int)

    def dfs_find_oil(i,j,visited,temp,count):
        move = [(-1,0),(0,1),(1,0),(0,-1)]
        temp.append((i,j))
        visited[i][j] = True

        for k in range(4):
            di = i+move[k][0]
            dj = j+move[k][1]
            if not (0<=di<len(land) and 0<=dj<len(land[0])):
                continue
            if visited[di][dj]==False and land[di][dj] == 1:
                count = dfs_find_oil(di,dj,visited,temp,count+1)

        return count

    def set_dic(lst,count):
        s = set()
        for item in lst:
            s.add(item[1])
        s_l = list(s)
        for i in s_l:
            y_dic[i] += count

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == False:
                temp = []
                count = dfs_find_oil(i,j,visited,temp,1)
                set_dic(temp,count)
    answer = 0
    print(f'y_dic = {y_dic}')
    for i in range(len(land[0])):
        answer = max(y_dic[i],answer)
    print(f'answer = {answer}')


    return answer
#land = [[0, 0, 0, 1, 1, 1, 0, 0],
#        [0, 0, 0, 0, 1, 1, 0, 0],
#        [1, 1, 0, 0, 0, 1, 1, 0],
#        [1, 1, 1, 0, 0, 0, 0, 0],
#        [1, 1, 1, 0, 0, 0, 1, 1]]
#land = [1]
land = [[0,1]]
#land = [[1],[1]]
print(solution(land))
