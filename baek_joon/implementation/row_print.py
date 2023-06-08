import sys
input = sys.stdin.readline

while True:
    input_str = input()
    if input_str == '\n':
        break
    elif input_str == '':
        break
    print(input_str, end='')

