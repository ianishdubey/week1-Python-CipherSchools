# Exercise,Number guessing game
# Make a variable like winning_number and assign any number to it.
# Ask user to guess a number
# if user guessed correctly then print "You Win !!!!"
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher  than actual number then print "too high"
    # bonus
    # google "how to generate random number in python" to generate random
    #winning number

    # Exercise Solution
winning_num = 69
user_num = int(input("guess a number betwee 1 to 100: "))
if user_num==winning_num:
    print("You win!!!!")
else:
    if user_num < winning_num:
        print("too low")
    else:
        print("too high")