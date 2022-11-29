#Ask the user to input 3 numbers and you have to print average of three numbers using string formatting
# Try to take all three comma seperated inputs in one line

num1,num2,num3=input("Enter your numbers seperated by comma: ").split(",")

average = (int(num1)+int(num2)+int(num3))/3
print(f"average of three numbers is {average}")

#another way of taking input
num1=int(input("Enter your 1st number: "))
num2=int(input("Enter your 2nd number: "))
num3=int(input("Enter your 3rd number: "))
average = (num1+num2+num3)/3
print(f"average of three numbers is {average}")