cars=['audi','bmw','lexus','ferrari','porshe']

for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.title())
car='audi'
print(car.title()=='Audi')

requested_topping='anchovies'
if requested_topping!='anchovies':
	print('Hold the anchovies')
else:
	print(requested_topping.title())


banned_users=['asepe','asekun','eyinju']
user='marie'
if user not in banned_users:
	print(f'\n{user.title()}, you can type a response.')


car='subaru'
print("Is car=='subaru'? I predict True")
print(car=="subaru")

print('\nIs car=="audi"? I predict False')
print(car=="audi")

age=66
if age<=18:
	print("\nYou're too young to vote.")
	print("Wait until you're 18 so you can vote")
else:
	print("\nYou're old enough to vote.")
	print("Have you gotten your voters card yet?")

age = 43
if age < 4:
	price=0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 60

print(f"Your admission cost is ${price}")

