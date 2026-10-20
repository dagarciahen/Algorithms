"""
Happy Number

In number theory, a happy number is defined as a number that, when repeatedly subjected
to the process of squaring its digits and summing those squares, eventually leads to 1.
An unhappy number will never reach 1 during this process, and will get stuck in an infinite loop.

Given an integer, determine if it is a happy number.

Example:
Input: n = 23
Output: True
Explanation:
23 -> 13 -> 10 -> 1
"""


def is_happy_number(n):
    slow = fast = n

    while True:
        if fast == 1: return True
        fast = next_number(next_number(fast))
        slow = next_number(slow)
        if fast == slow: return False

    return True



def next_number(x):
    suma = 0
    while x > 0:
        digit = x%10
        x = x//10
        suma += digit**2
    return suma


def run_test(n, expected, test_name):
    print(test_name)
    print("n        = " + str(n))
    print("expected = " + str(expected))

    try:
        actual = is_happy_number(n)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test(23, True, "Test 1")
    run_test(19, True, "Test 2")
    run_test(2, False, "Test 3")
    run_test(1, True, "Test 4")
    run_test(116, False, "Test 5")
