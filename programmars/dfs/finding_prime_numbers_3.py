from itertools import permutations
def solution(n):
    a = set()
    for i in range(len(n)):
        print(f'permutations() = {list(permutations(list(n), i + 1))}')
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    print(f'a = {a}')
    a -= set(range(0, 2))
    print(f'a = {a}')
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)

numbers = "011"
print(solution(numbers))


