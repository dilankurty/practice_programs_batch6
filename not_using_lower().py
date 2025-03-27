# Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

# prompt the user to input a string
string = input("Input a string: ")

# create a translation table
translation = str.maketrans("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ", "abcdefghijklmnñopqrstuvwxyz")

# convert the string to lower case using translation table method
lower = string.translate(translation)

# print the string in lower case
print(lower)