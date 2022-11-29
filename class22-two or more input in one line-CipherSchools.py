# We can take more than one input from the user in one line only

# using split function we can take multiple user input from user in one line

print("(,) should be used as seperator between name and age")
name,age = input("enter your name and age ").split(",")#here "," is used as seperator while giving input it is used
print(name)
print(age)
#if during giving input the term which is to be used as seperator is not used by user then output will be error