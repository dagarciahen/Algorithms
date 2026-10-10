"""
Substring Anagrams

Given two strings, s and t, both consisting of lowercase English letters,
return the number of substrings in s that are anagrams of t.

An anagram is a word or phrase formed by rearranging the letters of another
word or phrase, using all the original letters exactly once.

Example:
Input: s = "caabab", t = "aba"
Output: 2

Explanation:
There is an anagram of t starting at index 1 and another starting at index 2.
"""


def count_substring_anagrams(s, t):
    raise NotImplementedError()


def run_test(s, t, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print('t        = "' + t + '"')
    print("expected = " + str(expected))

    try:
        actual = count_substring_anagrams(s, t)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("caabab", "aba", 2, "Test 1")
    run_test("abab", "ab", 3, "Test 2")
    run_test("aaaaa", "aa", 4, "Test 3")
    run_test("abcdef", "gh", 0, "Test 4")
    run_test("abc", "abcd", 0, "Test 5")
