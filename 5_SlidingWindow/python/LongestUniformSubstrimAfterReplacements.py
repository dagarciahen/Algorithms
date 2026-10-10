"""
Longest Uniform Substring After Replacements

A uniform substring is one in which all characters are identical.
Given a string, determine the length of the longest uniform substring
that can be formed by replacing up to k characters.

Example:
Input: s = "aabcdcca", k = 2
Output: 5

Explanation:
If we can replace at most 2 characters, the longest uniform substring
we can achieve is "ccccc", obtained by replacing 'b' and 'd' with 'c'.
"""


def longest_uniform_substring_after_replacements(s, k):
    raise NotImplementedError()


def run_test(s, k, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = longest_uniform_substring_after_replacements(s, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("aabcdcca", 2, 5, "Test 1")
    run_test("aaaa", 2, 4, "Test 2")
    run_test("ababa", 1, 3, "Test 3")
    run_test("abcde", 1, 2, "Test 4")
    run_test("baaab", 2, 5, "Test 5")
