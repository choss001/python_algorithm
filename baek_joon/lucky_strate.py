strInt = input()

left = strInt[:len(strInt)//2]
right = strInt[-len(strInt)//2:]

temp = int(left)
leftSum = 0
while temp:
    leftSum += temp % 10
    temp = temp // 10

temp = int(right)
rightSum = 0
while temp:
    rightSum += temp % 10
    temp = temp // 10
print('LUCKY' if rightSum == leftSum else 'READY')
