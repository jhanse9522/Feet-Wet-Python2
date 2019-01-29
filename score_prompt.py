prompt = ("Enter score: \n")


try:
	grade = input(prompt)
	if .9 <=float(grade) <= 1:
		print("A")
	if .8 <= float(grade) < .9:
		print("B")
	if .7 <=float(grade) < .8:
		print("C")
	if .6 <=float(grade) < .7:
		print("D")
	if  float(grade) < .6:
		print("F")
	

except:
	print("Bad score!")
	