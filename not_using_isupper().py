# Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

# prompt the user to input a string
string = input("Input a string: ")

# check if all characters of the string is on upper case
if string == string.upper():
    result = True

# print the result
print(result)