"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, inp_str: str) -> bool:
        stack = []
        balanced = True
        if inp_str:
            for element in inp_str:
                if element in '({[':
                    stack.append(element)
                else:
                    if not stack:
                        balanced = False
                    else:
                        out = stack.pop()
                        if out + element in ['()','{}','[]']:
                            continue
                        else:
                            balanced = False
                            break

        if stack:
            balanced = False
        return balanced
