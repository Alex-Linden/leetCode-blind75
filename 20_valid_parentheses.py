"""Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""grab the last item in the string
if it is a closing bracket add to the stack
if it is an opening bracket compare to the last item in the stack
if they match move remove them from the stack and move to the next item in the string
if they don't match return false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "([{"
        closing = ")]}"
        valid_pairs = '() {' + '} []'

        for c in reversed(s):
            if c in closing:
                stack.append(c)
            elif c in opening:
                if len(stack) == 0:
                    return False
                if c + stack.pop() not in valid_pairs:
                    return False

        return len(stack) == 0
