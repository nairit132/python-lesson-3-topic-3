a = input('Enter a word:  (CAPS ONLY)')
print("The code will find A in the word you selected")
for i in a:
    if ( i =='A'):
        print("A is found")
        break
    else:
        print("A is not found")
