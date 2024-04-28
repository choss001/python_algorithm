def get_right_number(name):

    last_number = 0 
    for i in range(len(name)-1, -1, -1):
        if name[i] != 'A':
            last_number = i
            break
    middle_number = 0
    if name[1] == 'A':
        for i in range(len(name)):
            if name[i] != 'A':
                middle_number = i
                break
    else:
        for i in range(len(name)):
            if name[i] == 'A':
                middle_number = i
                break
    after
    print(f'last_number = {last_number}, middle_number={middle_number}')
    return max(last_number, middle_number)

def solution(name):
    print(get_right_number(name))
    return
#name = "JEROEN"




#first char along with 'A'
#go nomal vs go until not 'A' was found and backward
#
#first char along with not 'A'
#go nomal vs go until 'A' was found and backward

name = "JAN"
name = "JNAN"
print(solution(name))
