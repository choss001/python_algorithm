num = int(input())
count = sum = start = end = 1
while end != num:
    if sum == num:
        count += 1
        end += 1
        sum += end
    elif sum > num:
        sum -= start
        start += 1
    else:
        end += 1
        sum += end
print(count)
