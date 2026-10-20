"""
Longest Substring With Unique Characters

Given a string, determine the length of its longest substring
that consists only of unique characters.

Example:
Input: s = "abcba"
Output: 3

Explanation:
Substring "abc" is the longest substring of length 3 that contains
unique characters. "cba" also fits this description.
"""


def longest_unique_substring(s):
    hashSet = set()
    words= s
    left = 0
    right = 0
    count = 0
    length = 0
    
    for right in range(len(words)):
        while words[right] in hashSet:
            hashSet.remove(words[left])
            left +=1
        length = max(right-left+1, length)
        hashSet.add(words[right])
    return length





"""
COMPLEXITY ANALYSIS


runntime complexity is o(n) I traverse the string only once the words[right] in hashSet is o(1)
space complexity is o(m) as we use the hashset to store the elements and m is the total number of unique character



"""

            
    




def run_test(s, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print("expected = " + str(expected))

    try:
        actual = longest_unique_substring(s)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("abcba", 3, "Test 1")
    run_test("aaaaa", 1, "Test 2")
    run_test("abcdef", 6, "Test 3")
    run_test("", 0, "Test 4")
    run_test("pwwkew", 3, "Test 5")
