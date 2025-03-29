# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

# prompt the user to input a multiple line string
string_list = []

while True:
    string = input("Input a string(press enter to stop): ")
    if string == "":
        break
    else:
        # add right spaces to the string
        string_list.append(string + " " * (50 - len(string)))

# print the result
for string in string_list:
    print(string)