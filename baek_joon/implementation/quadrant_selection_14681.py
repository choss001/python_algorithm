import sys
input = sys.stdin.readline

ix = int(input())
iy = int(input())
if ix > 0 and iy > 0:
    print(1)
if ix> 0 and iy < 0:
    print(4)
if ix < 0 and iy > 0 :
    print(2)
if ix < 0 and iy < 0 :
    print(3)
