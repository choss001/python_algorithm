import sys
input = sys.stdin.readline

def binary_search(start, end, target,n, answer):
    mid = (start+end) // 2
    print(f'start ={start}, end = {end}, mid = {mid},answer = {answer}')
    if start > end:
        return answer
    if n[mid] > target:
        answer = binary_search(start, mid-1, target, n, answer)
    elif n[mid] <= target:
        answer = binary_search(mid+1, end, target, n, mid)
#   else:
#       answer = binary_search(mid+1, end, target, n, mid)

    
    return answer

def solution(n):
    n.sort()
    print(n)
    print(binary_search(0, len(n)-1, -1, n, -1))
    
    
    return 0

n = [3, 5, 20, 10, 16, 20, 10, 9, 8, 7, 11, 18, 25, 10, 10, 10, 10, 10, 10, 10, 10]
print(solution(n))

