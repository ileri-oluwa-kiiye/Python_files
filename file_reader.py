with open('pi_digits.txt') as content:
	lines= content.readlines()

pi_string=''
for line in lines:
	pi_string+= line.strip()

with open('learning_python.txt') as summary:
	ileri= summary.read()
	

with open('learning_python.txt') as summary:
	for lines in summary:
		lines.rstrip()

with open('learning_python.txt') as summary:
	ileri=summary.readlines()

this=''
for lines in ileri:
	this+=lines.lstrip()

this

with open('programming.txt', 'w') as file_object:
	"""I'm making changes to the programming.txt file from here"""
	file_object.write('I love programming.\n')
	file_object.write('I love creating new games.\n')
#To append the contents of a file:
with open('programming.txt', 'a') as file_object:
	file_object.write('I also love finding meaning in large datasets.\n')
	