import sys
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())

