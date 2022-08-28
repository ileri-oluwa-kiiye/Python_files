def make_shirt(size, text):
	print(f"We're printing your shirt of size {size} already.")
	print(f"The text '{text}' would be printed on it.\n")

make_shirt(16, 'Ilerioluwakiiye')

#defining the second function
texts=['Hello','Nice to meet you','I hope you are fine']
sent_messages=[]

def show_messages(message):
	print(message)

for text in texts:
	show_messages(text)
while texts:
	ask=texts.pop()
	sent_messages.append(ask)
 
print(f"\n{sent_messages}")
print(texts)

#defining another function
def make_pizza(size, *toppings):
	print(f"\nMaking a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(topping)
make_pizza(16, 'mushrooms', 'pepper', 'cheese')


#Function no. 4
def build_profile(first, last, **user_info):
	#build a dictionary containing everything we know about a user
	user_info['first_name']=first
	user_info['last_name']=last
	return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

