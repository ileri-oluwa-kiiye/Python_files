sandwich_orders=['chicken', 'bread', 'hotdog']
finished_sandwiches=[]

for sandwich_order in sandwich_orders:
	print(f"I have finished making your {sandwich_order.title()} sandwich.")
print('\nAll the sandwiches that were made include:')
while sandwich_orders:
	yes=sandwich_orders.pop()
	finished_sandwiches.append(yes)
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich)

def build_profile(first, last, **user_info):
	#build a dictionary of user profiles
	user_info['first_name']=first
	user_info['last_name']=last
	return user_info

user_profile= build_profile('albert', 'einstein', location= 'princeton', field= 'physics')
print(user_profile)

