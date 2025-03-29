# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function.

# prompt the user to input a string
string = input("Input a string: ")

# add zero at the beginning of the string (if the string is less than 5 characters)
if len(string) < 5:
    string = "0" * (5 - len(string)) + string

# print the result
print(string)