# Execrise-Watch COCO
# Ask user name and age
# if user name starts with ('a' or 'A') and age is above 10 then
# print 'You can watch coco movie'
# else print('Sorry,you cannot watch coco')

# Exercise solution
name = input("Enter your name: ")
age = input("Enter your age: ")
age=int(age)
if (name[0]=="a" or name[0]=='A') and age > 10:
    print("You can watch coco movie")
else:
    print("Sorry,you cannot watch coco")