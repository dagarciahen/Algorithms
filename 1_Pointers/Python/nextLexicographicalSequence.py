"""
Given a string of lowercase English letters, rearrange the characters to form a new string representing the next
immediate sequence in lexicographical (alphabetical) order. If the given string is already last in lexicographical
order among all possible arrangements, return the arrangement that's first in lexicographical order.

Example:
Input: s = "abcd"
Output: "abdc"
"""


def next_lexicographical_sequence(s: str) -> str:
    wordsList = list(s)
    right = len(s)-1
    while right > 0 and wordsList[right] <= wordsList[right-1]:
        right -= 1
    if right == 0:
        return "".join(reversed(wordsList))
    pivot = right-1
    right = len(s)-1
    while wordsList[pivot] >= wordsList[right]:
        right -= 1
    wordsList[pivot], wordsList[right] = wordsList[right], wordsList[pivot]
    wordsList[pivot+1:] = reversed(wordsList[pivot+1:])
    return "".join(wordsList)


    


def run_test(input_value: str, expected: str, test_name: str) -> None:
    print(test_name)
    print("input    = " + repr(input_value))
    print("expected = " + repr(expected))

    try:
        actual = next_lexicographical_sequence(input_value)
        print("actual   = " + repr(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("abcd", "abdc", "Test 1")
    run_test("dcba", "abcd", "Test 2")
    run_test("abdc", "acbd", "Test 3")
    run_test("aabb", "abab", "Test 4")
    run_test("abcedda", "abdacde", "Test 5")
    run_test("z", "z", "Test 5")


"""
def next_lexicographical_sequence(s: str) -> str:
    wordsList = list(s)
    right = len(s)-1
    while right > 0 and wordsList[right] <= wordsList[right-1]:
        right -= 1
    if right == 0:
        return "".join(reversed(wordsList))
    pivot = right-1
    right = len(s)-1
    while wordsList[pivot] >= wordsList[right]:
        right -= 1
    wordsList[pivot], wordsList[right] = wordsList[right], wordsList[pivot]
    wordsList[pivot+1:] = reversed(wordsList[pivot+1:])
    return "".join(wordsList)
"""