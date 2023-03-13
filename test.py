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