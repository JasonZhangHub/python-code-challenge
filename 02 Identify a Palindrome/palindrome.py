import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1] # slicing
    # reverse a string is to create a slice that starts with the length of the string, and ends at index 0
    return forwards == backwards

if __name__ == '__main__':
    print(is_palindrome('hello world'))
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))