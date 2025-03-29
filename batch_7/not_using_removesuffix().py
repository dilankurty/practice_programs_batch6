# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

# prompt the user to input a string
string = input("Input a string: ").lower()

# check if the suffix is used ("ed") and remove it from the string
if string.endswith("ed"):
    string = string[:-2]

# print the result
print(string)