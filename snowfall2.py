snowfall = [3,5,10,14,0,9]
weeks = 0
total = 0
print("The list of snow accumulation in inches by week:" + str(snowfall))
for snow in snowfall:
	weeks += 1   #(when you are counting, you are adding a constant amount, 1 in this case, to a variable pointing to zero)
	#total += total + snow 
	total +=snow
	print("loop week: " + str(weeks)) # when you want to see the loops happening, print within the loop.
	print("in process total: " + str(total))

print("final week: " + str(weeks)) #when you just want to see the end results, print outside of the loop.
print("final total: " + str(total))


#total = total + total + snow

#	0       0        3   

#total = 3

#total = 3 + 3 + 5

 
total = 0  #don't forget to reassign total back to zero to do this in same program here.

for snow in snowfall[:-3]: # using indices to loop over a segment of the sequence (snowfall). Here, it's used to accumulate snow amount for indices 0, 1, 2.
	total += snow
	print("\n a LOOP IN PROCESS partial list of snow accumulation including the first 3 weeks: \n" + ("\n" * 3) + str(total))
print("\na partial list of snow accumulation including the first 3 weeks FINAL AMOUNT: " + str(total))

def snow_tracker(snowfall_list): # this is making a function (encapsulation) for recording snow amount and weeks recorded. Any list of values can be passed in and the number of items will be tracked (representing weeks in this case) and the sum of those values included in the list.

	weeks = 0
	total = 0

	for snow in snowfall:
		weeks += 1
		total += snow
		print("Loop Week: " + str(weeks))
		print("Loop Total: " + str(total))
	print("Final Week: " + str(weeks))
	print("Total Accumulation: " + str(total))
	#return total
	#return weeks

snow_tracker(snowfall)

			


