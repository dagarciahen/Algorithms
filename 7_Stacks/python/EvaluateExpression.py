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
    stack = []
    res, sign, curr_num = 0, 1, 0
    for c in s:
        if c.isdigit():
            curr_num = 10*curr_num + int(c)
        elif c == '+' or c == '-':
            res = curr_num*sign 
            sign = 1 if c == '+' else -1
        elif c == '(':
            stack.push(res)
            stack.push(sign)
            curr_num = 0, sign = 1
        elif c == ')':
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    return res + curr_num*sign





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
