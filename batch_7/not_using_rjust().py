# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

# prompt the user to input a multiple line string
string_list = []

while True:
    string = input("Input a string(press enter to stop): ")
    if string == "":
        break
    else:
        # add left spaces to the string
        string_list.append(" " * (50 - len(string)) + string)

# print the result
for string in string_list:
    print(string)