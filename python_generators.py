from tkinter import N


def my_generator():
    n = 1
    print("This is printed first")
    yield n

    n += 1
    print("This is printed next")
    yield n

    n += 1
    print("This is printed last")
    yield n

a = my_generator()

print(a)
next(a)
next(a)
next(a)

for item in my_generator():
    print(item)


def reverse_string(my_string):
    length = len(my_string)
    for name in range(length -1, -1, -1):
        yield my_string[name]

print(f'\n')
for name in reverse_string('chart'):
    print(name)

    
    

