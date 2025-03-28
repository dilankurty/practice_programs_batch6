# Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

# prompt the user to input a string
string = input("Input a string: ")

# create a translation table
translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

# using for loop, iterate through the string to tramslate each character
for char in string:
    # print the result
    print(char.translate(translation_table), end="")