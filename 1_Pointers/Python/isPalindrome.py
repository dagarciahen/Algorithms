"""
Palindrome Check

Given a string, determine if it is a palindrome after removing all
non-alphanumeric characters and ignoring capitalization.

Example:
Input: s = "a dog! a panic in a pagoda."
Output: True
"""


def is_palindrome(s: str) -> bool:
    new_str = ""
    for ch in s:
        if ch.isalnum():
            new_str += ch
    i = 0
    j = len(new_str) -1
    while i < j:
        if new_str[i] != new_str[j]:
            return False
        i +=1
        j -=1
    return True



def run_test(s: str, expected: bool, test_name: str) -> None:
    print(test_name)
    print("s        = " + repr(s))
    print("expected = " + str(expected))

    try:
        actual = is_palindrome(s)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("a dog! a panic in a pagoda.", True, "Test 1")
    run_test("race a car", False, "Test 2")
    run_test("A man, a plan, a canal: Panama", True, "Test 3")
    run_test("", True, "Test 4")
    run_test("0P", False, "Test 5")

