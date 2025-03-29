# Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

# prompt the user to input a string
string = input("Input a string: ")

# check the location of the parameter in the string
for i in range(len(string)):
    if string[i] == "a":
        index = i
        break

# print the result
