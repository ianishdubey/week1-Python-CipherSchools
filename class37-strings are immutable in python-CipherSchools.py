#strings are immutable
#strings defined cannot be changed
string="string"

#with replace method only new string can be formed but original cannot be changed
string.replace('t','T')

print("string")# this print will give old value of string 

#as to get changed value of string firstly it would have to store in new variable
str=string.replace('t','T')
print(str)