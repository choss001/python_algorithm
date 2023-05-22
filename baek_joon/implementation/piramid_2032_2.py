m,n,a,b,c,d = 8, 5, 5, 3, 2, 1
location_map = [
    [1, 5, 10, 3, 7, 1, 2, 5],
    [6, 12, 4, 4, 3, 3, 1, 5],
    [2, 4, 3, 1, 6, 6, 19, 8],
    [1, 1, 1, 3, 4, 2, 4, 5],
    [6, 6, 3, 3, 3, 2, 2, 2]
]

piramid_sum = {}

#width
for i in range(m - a + 1):
    #height
    for j in range(n - b + 1):
        result_map = [location_map[i][j:j+a] for i in range(j, j+b)]
        piramid_sum[j,i] = sum(sum(result_map,[]))
        print(piramid_sum)
