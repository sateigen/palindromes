import re

def is_palindrome(sentence):
    if sentence == []:
        return
    is_palindrome(sentence[1:])
    backwards.append(sentence[0])



def main():
    user_input = input("Please enter a string. ")

    user_input = user_input.lower()

    user_input = re.sub("[^A-Za-z0-9]", "", user_input)

    user_input = list(user_input)

    is_palindrome(user_input)


if __name__ == '__main__':
    main()
