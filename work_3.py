while True:
    string = input("Enter the string: ")

    if string:
        words = string.split()

        if len(words) > 1:
            break
        else:
            print("Enter the string with several words.")

    else:
        print("There is an empty string. Please, try again.")

final_string = "  ".join(words)
print(final_string)






