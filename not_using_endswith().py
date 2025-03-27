# Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

# prompt the user to input a string
string = input("Input a string: ")

# check if the end matches the parameter
if string[-3:] == "ful":
    result = True

# print the result
print(result)