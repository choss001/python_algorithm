x = int(input("Please enter an interger: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')
    


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))