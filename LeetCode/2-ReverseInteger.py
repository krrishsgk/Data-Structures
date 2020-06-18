"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within
 the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
 problem, assume that your function returns 0 when the reversed integer
 overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:

        sign = (x>0)-(x<0)
        x = abs(x)
        digits = [0]
        while(x > 0):
            digits.append(x%10)
            x = x // 10

        reverse = sign*int(''.join(map(str, digits)))
        return reverse*(-2**31 < reverse < 2**31)

        
