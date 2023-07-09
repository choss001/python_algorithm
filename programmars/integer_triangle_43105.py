
def solution(triangle):
    answer = 0
    triangle = [[0] + t + [0] for t in triangle]
    print(f'triangle = {triangle}')
    for i in range(1, len(triangle)):
        for j in range(1, i+2):
            print(f'i = {i}, j = {j} triangle[i-1][j-1]= {triangle[i-1][j-1]}, triangle[i-1][j]={triangle[i-1][j]}')
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
            print(f'max triangle[i][j] = {triangle[i][j]}')
    answer = max(triangle[-1])
    print(f'traingle = {triangle}')
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
