# Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

# prompt the user to input a string
string = input("Input a string: ")

# check if the prefix is used and remove it from the string
if string.startswith("un", "re", "in", "im", "de"):
    string = string[2:]

# print new string without the prefix