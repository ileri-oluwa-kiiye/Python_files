from array import *
arrays = array('i', [1,3,5,7,9])
for i in arrays:
    print(i)
#print(arrays[0])
#print(arrays[1])
#print(arrays[2])

arrays.append(11)
#for i in arrays:
#   print(i)


def reverse(list):
    w = 0
    for quantity in list:
        w += 1
    for items in range(w-1, -1, -1):
        print(list[items])
reverse(arrays)

del arrays[4]
print(arrays)