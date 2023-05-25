import sys
input = sys.stdin.readline
N = int(input())

word_list = [input() for _ in range(N)]

answer_list = []
for word in word_list:
    exist_w = []
    for i in range(len(word)):
        if i == 0:
            if i == len(word) -1:
                answer_list.append(word)
                break
            exist_w.append(word[i])
        elif word[i] != word[i-1]:
            if word[i] not in exist_w:
                if i == (len(word) -1):
                    answer_list.append(word)
                    break
                exist_w.append(word[i])
            else:
                break
        elif word[i] == word[i-1] and i == (len(word) -1):
            answer_list.append(word)
print(len(answer_list))
