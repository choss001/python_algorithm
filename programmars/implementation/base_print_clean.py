def solution(wallpaper):
    max_x, max_y = -1,-1
    min_x, min_y = 99999999, 99999999

    for yp in range(len(wallpaper)):
        for xp in range(len(wallpaper[0])):
            if wallpaper[yp][xp] == '#':
                min_x = min(min_x, xp)
                min_y = min(min_y, yp)
                max_x = max(max_x, xp)
                max_y = max(max_y, yp)
    print(f'max_x={max_x}, max_y={max_y}, min_x = {min_x}, min_y={min_y}')
    
    return [min_x,min_y,max_x+1,max_y+1]

wallpaper = [".#...", "..#..", "...#."]
print(solution(wallpaper))
