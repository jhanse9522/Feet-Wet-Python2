#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

prompt1 = "Enter hours: \n"
prompt2 = "Enter Rate: \n"
hours = input(prompt1)
rate = input(prompt2)
pay = float(hours) * float(rate) 
pay = round(pay, 2)
print("Your gross pay is: " + str(pay))

