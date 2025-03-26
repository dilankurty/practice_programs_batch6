# Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

# prompt the user to input a string
string = input("Input a statement: ")

# check if the first character is a space then remove it
while string[0] == " ":
    string = string[0:]

# print the string without space at the beginning
print(string)