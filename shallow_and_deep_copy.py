list1 = [[1,2,3], [4,5,6], [7,8,9]]
list2 = list1
print('List 1 -', list1)
print('List 2 -', list2)

list1.append([10, 11, 12])
print('List 1 -', list1)
print('List 2 -', list2)
#In this list2 is still equal to list1 even though only list1 was appended

import copy
old_list = [[1,2,3], [4,5,6]]
new_list = copy.copy(old_list)   #This is what we call shallow copy
print('old list -', old_list)
print('New list-', new_list)

old_list.append([7,8,9])
print('Old list -', old_list)
print('New list-', new_list)
#In this shallow, editing only the one you append becomes appended