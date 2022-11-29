#print() function
print("hello")
print("hello \" \' ") #used backslash to print double and single commas 

#escape sequence
print("line A \t line B")# \t is used to get space 
print("line A \n line B")# \n is used to print another word in another line
print("these are two backslash \\\\")# \\=\ so for 2 backslash 4 backslash are used

#escape sequence as normal text
print(r"line A \n line B") # r is used to print escape sequnce as normaltext

#variables
name="John Wick"
print(name)

name="Rowin Atkinson" # Now new value of name will get print instead of old value
print(name)

#naming rules for variables
# 1var="defender" 
#print(1var) <-- variable name cannot start with number as it gives error

va1rs="lofi" # number can be used in between variable name
print(va1rs)

#variable name can start with underscore
_pop="popped"
print(_pop)

#variable name neither start with special symbol nor special symbol be used in between variable name
# @lord="ignis"
# print(@lord) <-- it will give error

#l@rd="kokan"
# print(l@rd) <-- it also gives error

#convention for variable naming
var_char_one=123 #Snake case writing
print(var_char_one)

varCharOne="AK" #Camel case writing
print(varCharOne)