number=input("Enter number:")
number=int(number)
if number%2==0:
  print(f'Yes, the number {number} is even.')
else:
  print(f'No, the number {number} is not even.')

number=155
while number<=5:
  print(number)
  number +=1


while True:
  city='quit'

  if city=='quit':
    break

  else:
    print(f"I'd love to go to {city.title()}!")

current_number=0
while current_number<= 10:
  current_number+= 1
  if current_number%2==0:
    continue

  print(current_number)

