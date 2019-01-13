fhand = open("words.txt")
dicty = dict()
for line in fhand:
	words = line.split()
	for word in words:
		print(word)  # up to this point: reads words in words.txt, now need to store them as keys in a dictionary.
		dicty[word] = '10' 
		#print(dicty)   # add key/value pair to dicty (in this case, an empty dictionary) with each iteration of loop

		

print(dicty)

print("hi" in dicty) 