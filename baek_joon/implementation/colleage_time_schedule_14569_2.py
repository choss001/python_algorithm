import sys
input = sys.stdin.readline

subjects = []
for _ in range(int(input())):
    subject = 0
    for sj in map(int, input().split()[1:]):
        subject |= 1 << sj
        print(f'subject : {bin(subject)}')
    subjects.append(subject)


for _ in range(int(input())):
    student = 0
    for sd in map(int, input().split()[1:]):
        student |= 1 << sd

    cnt = 0
    for subject in subjects:
        if (subject & student) == subject:
            cnt += 1

    print(cnt)
