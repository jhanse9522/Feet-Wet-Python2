prompt = "Enter temperature in Celcius: \n"

celcius = input(prompt)

round = round((int(celcius) * 9/5) + 32)

print(str(round) + " degrees") 
