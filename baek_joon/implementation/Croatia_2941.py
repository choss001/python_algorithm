import sys
input = sys.stdin.readline

cro_str = input()

cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for cro in cro_list:
    while cro_str.find(cro) != -1:
        count += 1
        cro_str = cro_str[0:cro_str.find(cro)] + '&'*len(cro) + cro_str[cro_str.find(cro) + len(cro):]

for i in cro_str:
    if i != '&' and i != '\n':
        count+=1
print(count)
