"""
Valid Parenthesis Expression

Given a string representing an expression of parentheses containing the characters
'(', ')', '[', ']', '{', or '}', determine if the expression forms a valid
sequence of parentheses.

A sequence of parentheses is valid if every opening parenthesis has a
corresponding closing parenthesis, and no closing parenthesis appears before
its matching opening parenthesis.

Example 1:
Input: s = "([]{})"
Output: True

Example 2:
Input: s = "([]{)}"
Output: False
"""


def is_valid_parenthesis_expression(s):
    raise NotImplementedError()


def run_test(s, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print("expected = " + str(expected))

    try:
        actual = is_valid_parenthesis_expression(s)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("([]{})", True, "Test 1")
    run_test("([]{)}", False, "Test 2")
    run_test("()[]{}", True, "Test 3")
    run_test("([)]", False, "Test 4")
    run_test("", True, "Test 5")
