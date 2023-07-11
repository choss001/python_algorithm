
def solution(people, limit):
    answer = 0

    left, right = 0, len(people) -1
    people.sort()
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            answer += 1
        right -= 1


    return len(people) - answer

people = [70, 50, 80, 50]
print(solution(people, 100))
