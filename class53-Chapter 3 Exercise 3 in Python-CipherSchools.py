# exercise one of three
# sum of n natural numbers
# ask a user for natural numbers(n)
# print total from 1 to n

# Exercise Solution
n=int(input("Enter the number: "))
total = 0
i = 1
while i<=n:
    total+=i
    i+=1
print(f"Sum of numbers is {total}")