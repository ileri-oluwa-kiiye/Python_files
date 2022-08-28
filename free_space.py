print("Languages:\n\tPython\n\tC\n\tJavascript")

drinks=['fanta', 'coke', 'sprite', 'pepsi']
message= f"I had to drink three cups of {drinks[0].title()} and two cups of {drinks[3].upper()}"
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