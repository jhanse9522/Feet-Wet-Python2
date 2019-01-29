#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0




prompt1 = ("Enter hours: \n")

try:

	total_hours = float(input(prompt1))

	prompt2 = ("Enter rate: \n")

	rate = float(input(prompt2))


#total_hours = over + hours

#50 = 10 + 40

#10 (20 *1.5) + 40 * 20

	ot_rate = rate * 1.5


	ot_hours = total_hours - 40

	ot_pay = ot_rate * ot_hours


	reg_pay = 40 * rate

	total_pay = reg_pay + ot_pay

	print("Your total pay including overtime hours at premium  pay rate is: \n" + str(total_pay) + "\n" + "Not bad!!!")

except:

	print("Please enter numeric information.")


def computepay(hours, rate):

	ot_rate = rate * 1.5

	ot_hours = hours - 40

	ot_pay = ot_rate * ot_hours

	reg_pay = 40 * rate

	total_pay = reg_pay + ot_pay

	print("Your total pay including overtime hours is: " + str(total_pay))









