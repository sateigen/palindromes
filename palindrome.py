import re

def is_palindrome(sentence):
    # TODO: return True or False if the sentence is or isn't a palindrome
    pass


def main():
    user_input = input("Please enter a string. ")

    user_input = re.sub("[^A-Za-z0-9]", "", user_input)

    is_palindrome(user_input)


if __name__ == '__main__':
    main()
