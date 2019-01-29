to_do = []

to_do2 = []

friends = ["debbie", "nadbor", "chris", "nipun", "gayla", "trevor", "isabel", "div"]

things = ["dmv", "loan", "cards", "walgreens", "vet", "medicine", "ceu", "book_review"]

#to_do.extend(friends + things)

to_do.extend(friends)
to_do.extend(things)

to_do2.append(friends)
to_do2.append(things)



prompt = ("What day is it? Please use all lowercase letters. \n")

day = input(prompt)
if day == "monday":
	#print(to_do)
	print(to_do)
	#print(friends)


