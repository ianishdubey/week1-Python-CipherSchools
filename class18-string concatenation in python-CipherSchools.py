#strings
#collection of characters inside single and double quotes

first_name="Devil"
last_name="World"
full_name=first_name + last_name
print(full_name)

#string cannot add with number
#string add with only string
# print(first_name + 3) <-- it will give error
print(first_name + str(3)) #<-- not give error
print(first_name + "3") #<-- not give error

#multiply operator can be used between string and number
print(first_name * 3)