#  check empty or not
# important

name = "abc"
if name:#true if string is not empty
    print("string is not empty")
else:
    print("string is empty")


name = ""
if name:#true if string is not empty
    print("string is not empty")
else:
    print("string is empty")

#taking user input and then performing the code
name =input("enter your name: ")
if name:#true if string is not empty
    print(f"your name is {name}")
else:
    print("you didn\'t type anything")