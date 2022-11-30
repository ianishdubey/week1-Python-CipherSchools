#strings
name="logistics"

# string indexing
print(name[-1])

# string slicing
print(name[0:2])
print(name[5:])
print(name[:3])
print(name[:])
print(name[2:6:1])
print(name[-1:0:-1])

# take user input
user_name,age=input("enetr your name and age seperated by comma: ").split(",")
print(user_name)
print(int(age))

# len function
print(len(name))

# lower,upper,title method
print(name.lower())
print(name.upper())
print(name.title())

# find,replace,center method
r_pos = name.find("r")
r_pos_2=name.find("r",r_pos+1)
print(r_pos_2)

#****logistics****
print(name.center(17,"*"))

# strings are immutable
# name[2] ="s"  <-- we cannot change the value 
print(name.replace("h","H",1))# this command will print the new value of name but in new string
print(name)#but if again we give this command, the output will be as original only