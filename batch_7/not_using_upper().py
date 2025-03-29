# Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

# prompt the user to input a string
string = input("Input a string: ")

# create a translation table
translation = str.maketrans("abcdefghijklmnñopqrstuvwxyz", "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

# translate the string to upper case using translation table method

# print the string in upper case