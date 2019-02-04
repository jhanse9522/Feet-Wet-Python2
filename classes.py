class MyClass:
	x = 5

#object = MyClass()

#print(object.x)


class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


client1 = Person("Jane", 18)

print(client1.name)

print(client1.age)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

class Dogs:
	def __init__(self, type, name, vet):
		self.type = type
		self.name = name
		self. vet = vet

fido = Dogs("terrier", "Fido", "Dr. Doolittle")

print(fido.vet)
print(fido.type)
print(fido.name)

class Employee:
	def __init__(self, name, age, town, salary = 50000):

		self.name = name  # structure is var name = value (the actual name value ("joe") will get initialized on the right side as the label on the left (self.name))
		self.age = age
		self.town = town
		self.salary = salary


	def nameFunc(self):  #you can name this parameter anything but the fact that is it the first parameter tells Python it is referencing the class itself
		print("hello, my name is: " + self.name)

	def townFunc(self):
		print("hello, my town is: " + self.town)




employee1 = Employee("Sheri", 56, "Colgate")

print(employee1.salary)
print(employee1.nameFunc()) #when calling a method versus accessing an attribute the only difference is you put parens after the dot notation syntax
print(employee1.townFunc())

employee1.age = 42  # attribute reassignment/modification

print(employee1.age)




