print("Languages:\n\tPython\n\tC\n\tJavascript")

drinks=['fanta', 'coke', 'sprite', 'pepsi']
message= f"I had to drink three cups of {drinks[0].title()} and two cups of {drinks[3].lower()}"
print(message)

drinks[0]='bigi'
print(drinks)

drinks.append('big')
drinks.append('idek')
print(drinks)

drinks.insert(0, 'ife')
print(drinks)

del drinks[0]
print(drinks)

print(drinks)
popped_drinks=drinks.pop(3)
print(popped_drinks)
print(drinks)

message=f"('He went to buy a {popped_drinks.title()} and added the rest which are {drinks})"
print(message)

too_gassy='sprite'
message= drinks.remove(too_gassy)
print(message)

message=f"Of all these {drinks}, I had to remove {too_gassy} because it was too gassy"
print(message)
