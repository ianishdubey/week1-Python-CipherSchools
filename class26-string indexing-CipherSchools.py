#string indexing in python

language="Python"

#position (index number)

# p=forward indexing-->0,backward indexing-->-6
# y=forward indexing-->1,backward indexing-->-5
# t=forward indexing-->2,backward indexing-->-4
# h=forward indexing-->3,backward indexing-->-3
# o=forward indexing-->4,backward indexing-->-2
# n=forward indexing-->5,backward indexing-->-1

print(language[0])
print(language[5])

# if user inputs position number excess thanthe positions of letters of a word than output will be index out of range
# print(language[8])<-- This will give error 

#if user want to print last letter of a word but user do not know the total number of words then user can use backward indexing starts with (-1)
print(language[-1]) 
print(language[-3])