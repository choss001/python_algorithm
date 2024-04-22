def solution():
    a,b = 12, 8
    def euclidean(a,b):
        if a%b == 0:
            return b
        elif b == 0:
            return a
        else:
            return euclidean(b,a%b)
solution()

