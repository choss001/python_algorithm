

def solution(name):
    up_down_count = 0
    #up_down_count
    min_move = len(name) * 2
    for i in range(len(name)):
        up_down_count += min(ord(name[i]) - ord('A') , ord('Z') + 1 - ord(name[i]))
        print(f'up_down_count = {up_down_count}, i = {i}')
    #right_left_count
        next_char = i + 1
        while next_char <len(name) and name[next_char] == 'A':
            next_char += 1
       
        print(f'i * 2 + (len(name) - next_char) = {i * 2 + (len(name) - next_char)}')
        print(f'i + (len(name) - next_char)*2 = {i + (len(name) - next_char)*2}')
        min_move = min(min_move, i * 2 + (len(name) - next_char), i + (len(name) - next_char)*2)

    print(f'min_move = {min_move}')
    return up_down_count + min_move

name = 'JSSZABY'    
print(solution(name))
