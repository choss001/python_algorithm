def solution(topping):
    answer = 0
    print(f'topping = {topping}')

    l, r = 0, len(topping)
    idx1 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        print(f'left={left}, right={right},m={m},l={l},r={r}, idx = {idx1}')
        if left < right:
            l = m + 1
        elif left >= right:
            idx1 = m
            r = m - 1
    print(f'idx1 = {idx1}')
    l, r = 0, len(topping)
    idx2 = 0
    while l <= r:
        m = (l + r) // 2
        left = len(set(topping[:m]))
        right = len(set(topping[m:]))
        print(f'left={left}, right={right},m={m},l={l},r={r}, idx = {idx2}')
        if left <= right:
            idx2 = m
            l = m + 1
        elif left > right:
            r = m - 1

    print(f'idx2 = {idx2}')
    answer = max(idx2 - idx1 + 1, 0)

    return answer
topping = [1, 2, 1, 3, 1, 4,6,4,2,1,3,5, 1, 2]

print(solution(topping))
