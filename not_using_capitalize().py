# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

# prompt the user to input a string
string = input("Input a string: ")

# convert the first character to uppercase and convert the rest of the characters to lowercase
string = string[0].upper() + string[1:].lower()

# print the result
print(string)