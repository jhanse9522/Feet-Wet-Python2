for fizzy in range(10):
	print("loop: fizzy")
	print("loop value of fizzy: " + str(fizzy))
print("last value of fizzy at end of loop: " + str(fizzy)) # this will print 9 because it is not counting. 9 is the last item in range.
#fizzy is initialized as a variable pointing to the VALUE (insert number here--in process of loop)
#print("some string") is printing what you tell it to print for however many items there are in the loop, the value of the items makes no difference
#print(fizzy) is saying to print what the variable points to at this moment. When using range as a sequence this will be whatever value is being looped over.


count = 0
total = 0

for i in range(20):
	print("loop value of i: " + str(i))
	count += 1
	print("in process count: " + str(count))
	total += i
	print("in process value total: " + str(total))

print("most recent value of i: " + str(i))
print("final count of items in range: " + str(count))
print("final cumulative value total of items in range: " + str(total))



tuple = (3,4,5,6,7)

myiter = iter(tuple) #iter method iterates over an iterable container   you can get iterators from iterable container objects

print(next(myiter))  #next method will move to the next in the sequence
print(next(myiter))
print(next(myiter))

#NOTE: the for loop creates an iterator object and executes a next method for each loop


