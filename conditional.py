available_toppings=['mushrooms', 'olives', 'green peppers', 'pepperoni','pineapple','extra cheese']
requested_toppings=['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f'Adding {requested_topping}, one minute please.')
	else:
		print(f"Sorry, we don't have {requested_topping}")
print("\nFinished making your pizza!")

#This is a 'try it yourself' exercise:
usernames=['admin','asepe','ileri','ife','asekun','mummy']
for username in usernames:
	if username=='admin':
		print(f'Hello {username}, would you like to see a status report?')
	else:
		print(f'Hello {username}, thank you for logging in again.')

#Exercise 2:
current_users=['ife','ileri','asepe','asekun','eyinju']
new_users=['tobi','gbemi','ife','ileri','olive']

for users in new_users:
	if users.lower() in current_users:
		print(f"\nUse a new username, username '{users}' has already been used")
	else:
		print(f"\nUsername '{users}' is available")


