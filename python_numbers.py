number= 50 + 6j
print(isinstance(number, float))
print(type(number))


from math import *
from msvcrt import kbhit
print(log(22))
print(sin(30))
print(factorial(23))

from random import *
Day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
print(choice(Day))

shuffle(Day)
print(Day)

x = 3

def f():
    global x
    x = 25

 
print(x)
print('After calling function f():')
f()
print(f'The value of x is now {x}')

def funct1():
    x = 20
    def funct2():
        global x
        x = 35
        

    print(f"Before calling funct2, x = {x}")
    funct2()
    print(f"After calling funct2, x = {x}")

funct1()

print(f"The global 'x' is now {x}")

#PYTHON ITERATORS
our_list = [3,66,775,66,725]
our_iter = iter(our_list)

print(next(our_iter))  #Prints the next value in a list or tuple
print(next(our_iter))
print(next(our_iter))
print(next(our_iter))
print(next(our_iter))


#Creating a custom iterator

