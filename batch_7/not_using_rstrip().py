# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

# prompt the user to input a string
string = input("Input a string: ")

# removes the space characters at the end of the string
while string[-1] == " ":
    string = string[:-1]

# print the result
print(string)