def make_decorated(func):
    def inner_function():
        print('This function just got decorated')
        func()

    return inner_function()

def simple_function():
    print('This is a simple function')

make_decorated(simple_function)
