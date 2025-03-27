# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# prompt the user to input a string
string = input("Input a string: ")

# add left spaces to the string
string = string + " " * 50

# print the result
print(string)