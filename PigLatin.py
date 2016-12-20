# Pig Latin Translator
# moves the first letter to the end and then append the suffix 'ay'

print 'Pig Latin Translator'

#Have the User enter a string and store the string into a variable original
original = raw_input("Enter a word:")

# Checks that the input is not empty by checking the length of the string
# Check that the input does not contain numbers
if len(original) > 0:
  # Change the original word to simplify 
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print "empty"
  
pyg = 'ay'


