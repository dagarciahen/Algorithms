"""
Repeated Removal of Adjacent Duplicates

Given a string, continually perform the following operation:
remove a pair of adjacent duplicates from the string.
Continue performing this operation until the string no longer contains
pairs of adjacent duplicates. Return the final string.

Example 1:
Input: s = "aacabba"
Output: "c"

Example 2:
Input: s = "aaa"
Output: "a"
"""


def remove_adjacent_duplicates(s):
    raise NotImplementedError()


def run_test(s, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print('expected = "' + expected + '"')

    try:
        actual = remove_adjacent_duplicates(s)
        print('actual   = "' + actual + '"')
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("aacabba", "c", "Test 1")
    run_test("aaa", "a", "Test 2")
    run_test("abba", "", "Test 3")
    run_test("azxxzy", "ay", "Test 4")
    run_test("abc", "abc", "Test 5")
