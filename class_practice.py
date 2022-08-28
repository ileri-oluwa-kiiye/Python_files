class Dog:
	"""A simple attempt to model a dog"""
	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name=name
		self.age=age
	
	def sit(self):
		"""Simulate a dog sitting in response to a command"""
		print(f"{self.name} is now sitting")

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(f"{self.name} rolled over!")

	def run(self):
		"""Simulate the dog running in response to a command"""
		print(f"The {self.age} old Dog is now running")

my_dog=Dog('Willie', 16)
Dog.roll_over(my_dog)
Dog.sit(my_dog)
Dog.run(my_dog)




class Restaurant:
	"""This class is to get the information of a restaurants"""
	
	def __init__(self, name, cuisine_type):
		self.name= name
		self.cuisine_type= cuisine_type

	def describe_restaurant(self):
		"""Print the information about the restaurant"""
		print(f"\nThe name of my restaurant is {self.name}.")
		print(f"The cuisine type is {self.cuisine_type}.")

	def open_restaurant(self):
		#Tell customers that the restaurant is still open
		print("The restaurant is open.")

"""I dont really have nice names for the lists, sorry"""
age=Restaurant('KFC', 'chicken')
aged=Restaurant('Item7', 'whole meals')
agin=Restaurant('Bread talk', 'bread')
thiss=[age, aged, agin]
for thisss in thiss:
	Restaurant.describe_restaurant(thisss)
	Restaurant.open_restaurant(age)




class User:
	"""Create an organised information about Users"""
	def __init__(self, first_name, last_name):
		"""Initialize attributs to describe users"""
		self.first_name= first_name
		self.last_name= last_name

	def describe_user(self):
		print(f"\nThe full name of this user is {self.last_name.title()} {self.first_name.title()}")

One=User('ilerioluwakiiye', 'abolade')
User.describe_user(One)