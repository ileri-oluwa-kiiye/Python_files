our_list = [3,66,775,66,725]
our_iter = iter(our_list)

print(next(our_iter))  #Prints the next value in a list or tuple
print(next(our_iter))
print(next(our_iter))
print(next(our_iter))
print(next(our_iter))

"""
class Pow_of_two:
    '''Class to implement an iterator of powers of two'''

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result

        else:
            raise StopIteration

print(Pow_of_two.__doc__)    #Print the comment under a class
a = Pow_of_two(4)

i = iter(a)
print(next(i))
print(next(i))
print(next(i))
"""

"""I dont know why this class is not running well. 
Therefore, I'm going to make it a comment.
Future me, if you have anything to do, do it!"""


a = [1, 2, 3, 4]
for i in a:
    print(i)

for i in range(1, 12, 2):
    print(i)
for i in range(1, 12, 3):
    print(i)