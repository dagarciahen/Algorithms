
s = "([])"
def valid_parenthesis_expression(s: str) -> bool:
    parenthesis_map = {'(':')','[':']','{':'}'}
    stack = []
    for c in s:
        if c in parenthesis_map:
            stack.append(c)
        else:
            if stack and parenthesis_map[stack[-1]] == c:
                stack.pop()
            else:
                return False
    return len(stack) == 0

def test():

    result = valid_parenthesis_expression(s)
    assert result is True

test()
