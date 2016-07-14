import re


def is_palindrome(sentence):
    if type(sentence) != list:
        sentence = sentence.lower()
        sentence = mash_string(sentence)
        print(sentence)
    if len(sentence) < 2:
        print(True)
        return True
    if sentence[0] != sentence[-1]:
        print(False)
        return False
    else:
        sentence.pop(0)
        sentence.pop(-1)
        is_palindrome(sentence)


def mash_string(sentence):
    return list(re.sub("[^A-Za-z]", "", sentence))



def main():

    if is_palindrome(input("Please enter a string. ")) == False:
        print("This is NOT a palindrome.")
    else:
        print("This is a palindrome")


if __name__ == '__main__':
    main()
