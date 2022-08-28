

class Base1:
    def function(self):
        print('Base1 is executing')


class Base2:
    def function2(self):
        print('Base 2 is executing')


class Derived(Base1, Base2):
    def Multifunction(self):
        print('Main class executing')

md1 = Derived()
md1.function()
md1.function2()
md1.Multifunction()