# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

# prompt the user to input a string
string = input("Input a string: ")

# add left and right spaces to the string
string = " " * 50 + string + " " * 50

# print the result
print(string)