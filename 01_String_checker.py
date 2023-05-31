# String checker function

def string_checker(question, valid_list, error):
    while True:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        for item in valid_list:
            if response == item or response == item[0]:
                return item

        print(error)
        print()
