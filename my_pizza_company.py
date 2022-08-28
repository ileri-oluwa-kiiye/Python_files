#find_anagrams("hello", "check") -->False
#find_anagrams("below","elbow")-->True

def find_anagram(word, anagram):
    list_1 =[]
    list_2 =[]
    #Seperate the letters of each string into lists
    
    for letters in word:
        list_1.append(letters)
    for letters in anagram:
        list_2.append(letters)
    
    a =sorted(list_1)
    b =sorted(list_2)
    #Arrange the elements of the lists for an accurate answer
    
    if a != b:
        return False
    else:
        return True

a =find_anagram('hello', 'check')
b = find_anagram('below', 'elbow')
print(a)
print(b)