numbers = []

num_to_enter = input("Enter a number: ")

num_list = list.append(num)


while True:
	inp = input("Enter a number: ")
	try:
		num = float(inp)
		total = total + num
		count += 1
	except:
		if inp.lower() == "done":
			break
		else:
			print("Please enter a valid number!")
			continue

	

print("total: ", total, "count: ", count, "average: ", total/count)

	
