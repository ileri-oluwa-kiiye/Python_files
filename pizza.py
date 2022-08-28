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

