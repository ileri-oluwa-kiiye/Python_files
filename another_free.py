dinner_guests=['ife', 'daddy', 'mummy']
invitation=(", you have been carefully selected to attend my dinner tomorrow at my mansion")

print(f"{dinner_guests[0].title()} {invitation}")
print(f"{dinner_guests[1].title()} {invitation}")
print(f"{dinner_guests[2].title()} {invitation}")

#Since ife won't be attending my dinner;
dinner_guests[0]='asepe'
print(dinner_guests)
#for the new set of my dinner guests
print(f"{dinner_guests[0].title()} {invitation}")
print(f"{dinner_guests[1].title()} {invitation}")
print(f"{dinner_guests[2].title()} {invitation}")

#my dinner table has just gotten bigger, more guests
dinner_guests.insert(0, 'asekun')
dinner_guests.insert(2, 'eyinju')
dinner_guests.append('bose')
print(dinner_guests)
print(f"{dinner_guests[0].title()} {invitation}")
print(f"{dinner_guests[1].title()} {invitation}")
print(f"{dinner_guests[2].title()} {invitation}")
print(f"{dinner_guests[3].title()} {invitation}")
print(f"{dinner_guests[4].title()} {invitation}")
print(f"{dinner_guests[5].title()} {invitation}")


message=",I'm so sorry, I can't invite you to my dinner"
print(f"{dinner_guests.pop(0).title()} {message} ")
print(f"{dinner_guests.pop(0).title()} {message} ")
print(f"{dinner_guests.pop(0).title()} {message} ")
print(f"{dinner_guests.pop(0).title()} {message} ")
print(dinner_guests)


print(f"{dinner_guests[0].title()} {invitation}")
print(f"{dinner_guests[1].title()} {invitation}")

del dinner_guests[0]
del dinner_guests[0]

print(dinner_guests)