# ask user for name
# Example - Anish Dubey
# print count for each word
# output
    # A : 1
    # N : 1
    # I : 1
    # S : 1
    # H : 1
    #   : 1
    # D : 1
    
    # Exercise solution

name = input("Please enter your name: ")
# Anish
# name.count("A"), name.count(name[0]) = 1
# name.count("n"), name.count(name[1]) = 1
# name.count("i"), name.count(name[2]) = 1
# name.count("s"), name.count(name[3]) = 1
# name.count("h"), name.count(name[4]) = 1
# output
    # A : 1
    # n : 1
    # i : 1
    # s : 1
    # h : 1
    
temp_var=""
i=0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
    print(f"{name[i]}:{name.count(name[i])}")
    i+=1