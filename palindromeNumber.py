"""
Given an integer x, return true if x is a palindrome, and false otherwise.
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?

"""

#String solution

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return list(str(x)) == list(reversed(list(str(x))))

#non-string method
class Sollution:
    def isPalindrome(self, x:int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed = 0
        original = x
        while x > reversed:
            reversed = reversed * 10 + x % 10
            x //= 10
        return x == reversed or x == reversed // 10
