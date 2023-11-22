import random

N = int(input())


#action = [True]*3 + [False]*7
a_action = [True]*14 + [False]*86
b_action = [True]*14 + [False]*86
c_action = [True]*14 + [False]*86

total_true_count = 0
c_count = 0

for _ in range(N):
    a = random.sample(a_action, k=1)[0]
    b = random.sample(b_action, k=1)[0]
    c = random.sample(c_action, k=1)[0]
    if a == True or b == True or c == True:
        total_true_count +=1
print(f'{total_true_count}')
print(f'{total_true_count/N * 100}')
