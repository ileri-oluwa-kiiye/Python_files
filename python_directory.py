import numbers
import os

print(os.getcwd())  #Returns the present working directory



print(os.getcwdb()) #Returns the directory as a byte document



#os.chdir('C:\\Users\\user pc\\Desktop\\python_work')    #Used to change directory

#print(os.listdir())   #List all the files and sub-directories present in a directory

os.mkdir('Test')   #Used to make a new directory under the present directory
os.rename('Test', 'New_test')    #Used to rename the subdirectory i.e. Test to New_test

#os.remove('Text.txt')    #Used to remove a file
os.rmdir('New_test')  #Used to remove a directory


