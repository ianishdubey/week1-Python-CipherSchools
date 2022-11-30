# problem
# ask user to input a number containing more than one digit
# example - 1256 
# calculate 1+2+5+6 and print

# algorithm - (method to solve problem in human language)
# ask input in string i.e. do not change string to int
# example -"1256"
# pick string character one by one and change to int
# int(example[0])+int(example[1])+int(example[2])+int(example[3])....go upto len(example) - 1

# Exercise Solution

n=input("Enter number containing more than one digit: ")
total = 0
i = 0
while i<len(n):
    total+=int(n[i])
    i+=1
print(total)
