#using strip method to solve problem with spaces

name="    Thor    "
dots="............."

#lstrip() method uses to remove left spaces
print(name.lstrip() + dots)

#rstrip() method uses to remove right spaces 
print(name.rstrip() + dots)

#strip() method uses to remove all left and right spaces 
print(name.strip() + dots)

#replace(" ","") method uses to remove all spaces
print(name.replace(" ","") + dots)



# Using the strip methods in chapter 2 exercise 3
word,single_character=input("input should be comma seperated: " ).split(",")
length=len(word)
small_word=(word.lower().strip())
small_char=(single_character.lower().strip())
times=small_word.count(small_char)
print(f"length of the word is {length}")
print(f"number of count of {single_character} is {times}")

