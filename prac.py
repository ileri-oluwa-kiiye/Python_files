class MyComplexNumber:
    """Constructor Methods"""

    def __init__(self, real=0, imag=0):
        """Initialize the characteristics of My complex number"""
        print("My complex number executing...")
        self.real_part = real
        self.imag_part = imag 

    def display_complex(self):
        print("{0} + {1}j". format(self.real_part, self.imag_part))

complex1 = MyComplexNumber(60,4)
print(complex1.display_complex())

this = 1
that = 3

print("{0}j and {1}i".format(this,that))

