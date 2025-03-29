# Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

# prompt the user to input a string
string = input("Input a string: ")

# check how many time the function parameter appear in the string
count = 0
for char in string:
    if char == "a":
        count += 1

# print the result
print(count)