a = lambda x:x**2
print('The square of 10 is', a(10))

#Lambda function is an anonymous function that is defined instead of an a
#i.e instead of using def, we use lambda

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0), my_list))
print(new_list)