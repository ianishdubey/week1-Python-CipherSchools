#take two comma seperated inputs from the user
# 1. User's name
# 2. single character
 
# output - 2 lines to be print in output
# 1.) User's name length
# 2.) Count the character that user inputed (bonus : case insensitive count)
  
word,single_character=input("input should be comma seperated: " ).split(",")
length=len(word)
times=word.count(single_character)
print(f"length of the word is {length}")
print(f"number of count of {single_character} is {times} ")