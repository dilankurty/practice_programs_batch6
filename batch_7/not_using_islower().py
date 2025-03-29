# Prog04. islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.

# prompt the user to input a string
string = input("Input a string: ")

# check if all characters of the string is on lower case
if string == string.lower():
    result = True
else:
    result = False

# print the result
print(result)
