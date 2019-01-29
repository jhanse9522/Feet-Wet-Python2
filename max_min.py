largest = None
smallest = None
try:
	while True:
    	num = float(input("Enter a number: "))
    	if num == "done":
        	break
    	
except:
    print("Invalid Input")
for intervar in [7, 2, 10, 4]:
    if largest is None or intervar > largest:
        largest=intervar
for intervar in [7, 2, 10, 4]:
    if smallest is None or intervar < smallest:
        smallest = intervar

print("Maximum", largest)
print("Minimum", smallest)