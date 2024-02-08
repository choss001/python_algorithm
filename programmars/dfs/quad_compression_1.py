def solution(arr):
    for i in arr:
        print(i)
    answer = [0, 0]

    def check(size, x, y):
        print(f'check!! size={size}, x={x}, y={y}')
        if size == 1:
            answer[arr[y][x]] += 1
            print(f'answer = {answer}')
            return
        else:
            first = arr[y][x]

            for dy in range(size):
                for dx in range(size):
                    print(f'dy={dy}, dx={dx}, first={first}, size={size}, y+dy={y+dy}, x+dx={x+dx}, x={x},y={y}')
                    print(f'arr[y+dy][x+dx] = {arr[y+dy][x+dx]}')
                    if first != arr[y + dy][x + dx]:
                        print(f'first != arr')
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1
    check(len(arr),0,0)


    return answer
arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
#arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
#arr = [[1,1],[1,1]]
print(solution(arr))
