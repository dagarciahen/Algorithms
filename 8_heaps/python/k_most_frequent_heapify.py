
"""
K Most Frequent Strings
Medium
Find the k most frequently occurring strings in an array, and return them sorted by frequency in descending order. If two strings have the same frequency, sort them in lexicographical order.

Input: strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], k = 2
Output: ['go', 'byte']

Explanation: The strings "go" and "byte" appear the most frequently, with frequencies of 3 and 2, respectively.

Constraints:
k ≤ n, where n denotes the length of the array.

"""


def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    pass



def run_test(strs, k, expected, test_name):
    print(test_name)
    print("strs     = " + str(strs))
    print("k        = " + str(k))
    print("expected = " + str(expected))

    try:
        actual = k_most_frequent_strings(strs, k)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test(['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go'], 2, ['go', 'byte'], "Test 1")
    run_test(['a', 'b', 'a'], 1, ['a'], "Test 2")
    run_test(['x', 'y', 'z'], 3, ['x', 'y', 'z'], "Test 3")
    run_test(['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2, ['i', 'love'], "Test 4")
    run_test(['aaa', 'aa', 'a', 'aaa', 'aa', 'a'], 1, ['a'], "Test 5")
