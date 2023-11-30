import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_lst = list(map(int, input().split()))
m_lst = list(map(int, input().split()))

nm_lst = n_lst + m_lst

nm_lst.sort()
answer = ' '.join(map(str, nm_lst))
print(f'{answer}')
