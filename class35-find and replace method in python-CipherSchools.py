# replace() method
string ="she is beautiful and she is good dancer"
print(string.replace("is","was",2)) #replace method replace teh word we want to replace

#find() method
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)