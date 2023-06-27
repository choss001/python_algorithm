n, c = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

array.sort()


def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = array[0]
        count = 1

        print()
        for i in range(1, len(array)):
            print(f'for in i = {i}, current = {current}, mid = {mid}, array[i] = {array[i]}, end = {end}, start = {start}, count= {count}')

            if array[i] >= current + mid:
                count += 1
                current = array[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start = 1
print(f'array[-1] = {array[-1]}')
print(f'array[0] = {array[0]}')
end = array[-1] - array[0]
answer = 0

binary_search(array, start, end)
print(answer)
