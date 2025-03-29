# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

# prompt the user to input a string
string = input("Input a string: ")

# check the location of the parameter "a" in the string starting from the last character
for i in range(len(string)-1, -1, -1):
    if string[i] == "a":
        index = i
        break

# print the result
print(index)
