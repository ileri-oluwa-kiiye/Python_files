print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("Enter the first number:")
    if first_number=='q':
        break 
    second_number=input("Enter the second number:")
    if second_number=='q':
        break
    answer= int(first_number/second_number)
    print(answer)