count = 0
total = 0

while True:
	inp = input("Enter a number: ")
	try:
		num = float(inp) # value I want to add to my accumulator, labelled as num (it's the float of the user input when they enter a valid number)
		total = total + num
		count += 1
	except:
		if inp.lower() == "done":
			break
		else:
			print("Please enter a valid number!")
			continue

	

print("total: ", total, "count: ", count, "average: ", total/count)


#Accumulator Pattern

#Steps:

#1) Establish your base
#2) Start your for loop and decide what you want to loop over
#3) Do your business (What do you want to do inside this for loop at each level?
#4) Determine the value that you want to accumulate (here, it's the user input)d or add to your accumulator (the base)
#5) Update your counter variable (+=1 or however many you want to count by each time you loop over something)

	
