tuple = ('w', 'e', 'l', 'c', 'o', 'm', 'e')

gr, am, br, cr, dr, ak, fwk = tuple
print(gr)
print(am)
print(tuple[1:7])
print(tuple[:-3])
print(tuple[3:])
print(tuple[:])
print(tuple.count('e'))
print(tuple.index('c'))

tuple4 = tuple

print(tuple4[3])

nest = ('point', [1,2,3], (5,6,7))
print(nest[0][3])
print(nest[1])



print(('agaim',)*4)

#Tuple operations
tuple = ('w', 'e', 'l', 'c', 'o', 'm', 'e')  #for easy reference to the tuple
for items in tuple:
    print(f"Letter '{items}' is in the tuple.")


#built in functions for tuples
print(tuple)       
print(max(tuple))    #print the maximum value
print(min(tuple))    #print the minimum value in the tuple
print(sorted(tuple))
print(len(tuple))

