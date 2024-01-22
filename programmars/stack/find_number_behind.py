import sys
input = sys.stdin.readline

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i, target in enumerate(numbers):
        while stack and numbers[stack[-1]] < target:
            answer[stack.pop()] = target
        stack.append(i)
    return answer
numbers = [9, 1, 5, 3, 6, 2]	

print(solution(numbers))
