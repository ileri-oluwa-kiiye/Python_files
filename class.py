class Dog:
	def __init__(self, name, age):
		self.name= name
		self.age=age

	def sit(self):
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		print(f"{self.name} rolled over!")



class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
 
	def get_descriptive_name(self):
			long_name = f"{self.year} {self.make} {self.model}"
			return long_name.title()
 
class Battery: 
	"""Print the type and year of a battery"""
	def __init__(self, type, year):
		self.type=type
		self.year=year

