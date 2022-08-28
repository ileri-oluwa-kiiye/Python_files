ileri = {'name':'Ilerioluwakiiye', 'age':'16','best_color':'green'}

favorite_languages={
	'jen':['java'],
	'sarah':['ruby'],
	'ileri':['python']
}

for name, languages in favorite_languages.items(): 
	print(f"\n{name.title()}'s favorite language is:")
	for language in languages:
		print(f"\t{language.title()}.")

Ilerioluwakiiye={
	'first_name':['Ilerioluwa'],
	'last_name':['Abolade'],
	'age':[16]
}

for title, subject in Ilerioluwakiiye.items():
	print(f" Ilerioluwakiiye's {title.title()} is:")
	for subjects in subject:
		print(f"\t{subjects}")
#Learning dictionary in a dictionary:
users={
	'aeinstein':{
	'first': 'albert',
	'last': 'einstein',
	'location': 'texas'
	},
	'ileri':{
	'first':'ilerioluwakiiye',
	'last':'abolade',
	'location':'russia',
	}
}

for username, user_info in users.items():
	print(f"\nUsername: {username.title()}:")
	full_name=f"{user_info['first']} {user_info['last']} /"
	location= f"{user_info['location']}"

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

#This is a dictionary in a dictionary
family_members={ 
	'Ifeoluwa': {
	'first_name':'ifeoluwa',
	'last_name':'abolade',
	'age': 'eighteen'
	},

	'Ilerioluwakiiye': {
	'first_name':'ilerioluwakiiye',
	'last_name':'abolade',
	'age': 'seventeen'
	}
}

for names, info in family_members.items():
	print(f"{names.title()}'s full name is {info['first_name'].title()} {info['last_name'].title()}")
	print(f"\tShe is {info['age']} years old.\n")

pages=['fifty', 'hundred', 'abey']
pages.sort()
print(pages)
for lis in pages:
  print(lis)


pets=['cats','dog','cats']
print(pets)

while 'cats' in pets:
	pets.remove('cats')

print(pets)