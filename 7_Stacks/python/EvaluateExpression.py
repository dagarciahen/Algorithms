"""
Evaluate Expression

Given a string representing a mathematical expression containing integers,
parentheses, addition, and subtraction operators, evaluate and return the result
of the expression.

Example:
Input: s = "18-(7+(2-4))"
Output: 13
"""


def evaluate_expression(s):
    raise NotImplementedError()


def run_test(s, expected, test_name):
    print(test_name)
    print('s        = "' + s + '"')
    print("expected = " + str(expected))

    try:
        actual = evaluate_expression(s)
        print("actual   = " + str(actual))
        print("pass     = " + str(actual == expected))
    except NotImplementedError:
        print("actual   = not implemented")

    print()


if __name__ == "__main__":
    run_test("18-(7+(2-4))", 13, "Test 1")
    run_test("1 + 2 - 3", 0, "Test 2")
    run_test("(10-(2+3))", 5, "Test 3")
    run_test("7", 7, "Test 4")
    run_test("20-(3-(2-1))", 18, "Test 5")
