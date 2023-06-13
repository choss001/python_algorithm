import sys
input = sys.stdin.readline

student_all = [0] * 30

for _ in range(28):
    S = int(input())
    student_all[int(S)-1] = 1

for i in range(30):
    if student_all[i] == 0:
        print(i+1)
