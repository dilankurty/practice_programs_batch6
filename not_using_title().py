# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

# prompt the user to input a string
string = input("Input a string: ")

# converts the first character to uppercase and converts the rest of the characters to lowercase
title = []

for word in string.split():
    title.append(word[0].upper() + word[1:].lower())

# print the result
print(" ".join(title))