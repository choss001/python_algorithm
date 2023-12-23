def divisor(number): # number : 16
    result = []
    print(f'number**(1/2)={int(number**(1/2))+1}')
    for i in range(1, int(number**(1/2))+1):
        if number%i==0:
            result.append(i)
            print(f'i = {i}, number//i = {number//i}')
            if i < number//i:
                result.append(number//i)
    result.sort() 
    return result 
print(divisor(16))
