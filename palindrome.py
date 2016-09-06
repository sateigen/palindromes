import re


def is_palindrome(sentence):
    if type(sentence) != list:
        sentence = sentence.lower()
        sentence = mash_string(sentence)
    if len(sentence) < 2:
        return True
    if sentence[0] != sentence[-1]:
        return False
    else:
        sentence.pop(0)
        sentence.pop(-1)
        return is_palindrome(sentence)


def mash_string(sentence):
    return list(re.sub("[^A-Za-z]", "", sentence))


def main():
    if is_palindrome(input("\nPlease enter a string: ")):
        print("\nThis is a palindrome.\n")
    else:
        print("\nThis is NOT a palindrome.\n")


if __name__ == '__main__':
    main()
