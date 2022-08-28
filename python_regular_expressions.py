import re

if re.search(" ape ",'The ape was at the apex'):
	#The re.search is used to find the occurences of the first string in the second,
	#It returns a True unless otherwise specified.+
	print('There is an ape')

allApes = re.findall("ape.", 'There is an ape in apes.')
	#findall() returns a list of matches
	#. is used to match any character/space

for i in allApes:
	print(i)
print('\n')

allAnimals = "Cat mat rat fat pat"

animal = re.findall("[crfpm]at", allAnimals)
	#Note that 'Cat' did not get printed here
for i in animal:
	print(i)

print('\n')
some_animals = re.findall('[c-mC-M]at', allAnimals)
	#the c-m means every letter between c and m. Case sensitive too
	#the C-M means every upper case between C and M.
for i in some_animals:
	print(i)

someanimals = re.findall("[^Cr]at", allAnimals)
	#the ^ mark means...every thing except...
print('\n')
for i in someanimals:
	print(i)



Owlfood = 'rat cat mat pat'
#to replace all matches in a string

regex = re.compile('[cr]at')
#this is to compile Cat and rat to one variable

substituted = regex.sub('owl', Owlfood)
print(substituted)

sentence = 'Here is a \\string'

print("Find \\stuff:", re.findall('\\\\string', sentence))
#You have to put two extra slashes to find the double slashes present before.
# re.findall('\\string', sentence) will not work for it.

#OR you could use the r"..." method which dosen't treat back slashes as special characters.
print("Find \\stuff:", re.findall(r'\\string', sentence))

random = "F.B.I.  I.R.S. CRS"
print('All matches:', re.findall('.\..\..', random))
#A period is used to depict any character

sentence = """This is a long string that 
goes on for many
many lines"""

regex = re.compile('\n')
"""
\b = backspace
\f = form feed
\r = carriage return
\t = tab
\v = Vertical tab
"""
random = regex.sub(" ", sentence)
print(random)