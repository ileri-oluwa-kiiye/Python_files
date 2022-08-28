words = 1
sentence = 'I have to count the number of words in this text.'
for character in sentence:
    if character == ' ':
        words += 1

print(words)