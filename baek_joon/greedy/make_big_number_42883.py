
number = input()
k = int(input())


def solution(number, k):
    stack = []
    for n in number:
        print(f'before stack = {stack}')
        print(f'n = {n}')
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
        print(f'after stack = {stack}')

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

print(solution(number, k))
