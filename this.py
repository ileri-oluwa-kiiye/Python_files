seat=['this','that','these','everytime','esio']

print('The first three items on the list are:')
first_three=seat[:3]
print(first_three)
print('\nThe middle items from the list are:')
print(seat[1:4])
print('\nThe last items on the list are:')
print(seat[2:5])
print('\n')
for items in seat:
	print(items)