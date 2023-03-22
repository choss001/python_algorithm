temp = 4
print(temp)

match temp:
    case 4:
        print("wow!!!")
    case 5:
        print("false")
    case _:
        print("why")

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		coutinue
	print("Found an odd number", num)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4) 
fruits.reverse()
fruits.append('grape')
fruits.sort()
fruits.pop()