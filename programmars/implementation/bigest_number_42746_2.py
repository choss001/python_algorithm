def solution(numbers):
    temp = list(map(str,numbers))
    temp.sort(key=lambda x : x*3, reverse=True)
    return ''.join(temp)

#numbers = [6,10,2]
numbers = [547,54,5]

print(solution(numbers))
