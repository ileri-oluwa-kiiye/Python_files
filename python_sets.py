
"""
    Sets are:
        mutable: editable
        not necessarily in order
        duplicates not allowed
        used to perform mathematical calculations
"""

#We can form a set from a list and make a list from the set

from ast import While
from os import setsid
from typing import FrozenSet


set1= {3, 4, 5,22,}
list1=list(set1)  #Making a list from a set
print(list1)

set1= set(list1)  #Making a set froma list
print(set1)

#Operations on a set
set = {1,3,4,5,6,7}

set.add(77)  #Add an object
print(set)

set.update([55, 33,332])      #Adding multiple items to a set
print(set)

set.update([42, 53], {33, 55,1233})    #Adding multiple items to the set


"""Remove and discard"""
set.remove(332)
print(set)

set.discard(42)   #Uncertain of whether or not its in the list; to avoid errors
print(set)

#Mathematical operations
print(set.union(set1))   
print(set.intersection(set1))

print(set - set1)  
#or print(set.difference(set1))

print(set.symmetric_difference(set1))
#prints every value except the intersection

print(2 not in set)    #Check if its not present in the set
print(77 in set)   #Check if its in the set


"""
    FrozenSets are immutable sets
    While tuples are immutable lists
"""