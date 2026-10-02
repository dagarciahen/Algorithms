"""
Given a string, determine if it's a palindrome after removing all non-alphanumeric characters. A character is alphanumeric if it's either a letter or a number.
Input: s = 'a dog! a panic in a pagoda.'
Output: True
"""

def isPalindrome(s: str) -> bool:
    new_s = ""
    n = len(s)
    for i in range(n):
        if ('a' < s[i] < 'z') or ( 'A' < s[i] < 'Z') or ( '0' < s[i] < '9'):
            new_s += s[i]
        ## new_s = "".join([char for char in s if char.isdigit()[)
    i = 0
    j = n-1
    while (i < j):
        if new_s[i] == new_s[j]:
            i += 1
            j -=1
            continue
        else:
            return False
        return True 

