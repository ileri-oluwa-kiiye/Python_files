class Pow_of_two:
    def __init__(self, max= 0):
        self.max= max

    def __iter__(self):
        self.n = 0

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result

        else:
            raise StopIteration


print(Pow_of_two.__doc__)
a = Pow_of_two(2)

i= iter(a)
print(next(i))
print(next(i))
print(next(i))