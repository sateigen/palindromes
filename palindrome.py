import re


def is_palindrome(sentence):
    if len(sentence) < 2:
        return True
    if sentence[0] != sentence[-1]:
        return False
    else:
        sentence.pop(0)
        sentence.pop(-1)
        is_palindrome(sentence)




def main():
    user_input = input("Please enter a string. ").lower()

    user_input = re.sub("[^A-Za-z0-9]", "", user_input)

    user_input = list(user_input)

    sentence = []

    sentence.append(user_input)

    is_palindrome(user_input)

    if is_palindrome(user_input):
        print("This is a palindrome.")
    else:
        print("This is NOT a palindrome")


if __name__ == '__main__':
    main()
