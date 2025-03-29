# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

# prompt the user to input a string
string = input("Input a string: ")

# check if the beginning matches the parameter
if string[:3] == "pre":
    result = True

# print the result
print(result)
