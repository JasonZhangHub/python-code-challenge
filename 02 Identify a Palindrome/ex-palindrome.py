import re

def palindrome(st):
    # step 1: extract only letters from the string
    string= "".join(re.findall("[a-zA-Z]+", st)).lower()
    
    # step 2: test whether the string is palindrome
    n = len(string)
    isPalindrome = True
    for i in range(n):
        if string[i]!= string[n-1-i]:
            isPalindrome = False
            break
        
    return isPalindrome