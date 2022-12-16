email = input("ENTER YOUR EMAIL: ")    # Take input from user
k, j, d = 0, 0, 0    # Initialize variables k, j, d with 0
if len(email) >= 6:    # Check if email address is greater than or equal to 6
    if email[0].isalpha() or email[0].isdigit():    # Check if first character is alphanumeric or not
        if "@" in email and email.count("@") == 1:    # Check if email address contain only one '@'
            if email[-4] == "." or email[-3] == ".":    # Check if email address contain '.' right before extension
                for i in range(len(email)):    # Iterate over all the characters of email address
                    if email[i].isspace():    # Check if email address contain any space
                        k = 1
                    elif email[i].isupper():    # Check if email address contain any upper case character
                        j = 1
                    elif email[i] == "_" or email[i] == "." or email[i] == "@":    # Check if email address contain any special character
                        continue    # Continue the loop
                    elif email[i].isdigit() or email[i].isalpha():    # Check if email address contain any alphanumeric character
                        continue    # Continue the loop
                    elif email[i] != "_" or email[i] != "." or email[i] != "@":    # Check if email address contain any other character rather than special characters
                        d = 1    # Set d=1
                if k == 1 or j == 1 or d == 1:    # Check if email address is valid or not
                    print("WRONG EMAIL 5")
                else:
                    print("RIGHT EMAIL")    # Print "RIGHT EMAIL" if email address is valid
            else:
                print("WRONG EMAIL 4")
        else:
            print("WRONG EMAIL 3")
    else:
        print("WRONG EMAIL 2")
else:
    print("WRONG EMAIL 1")