"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""

class Solution:
    def isValid(self, s:str) -> bool:
        openBrackets = ['(', '[', '{'] #store in list for ease and note that avoids duplication.
        closeBrackets = [')', ']', '}'] #store in list for ease and note that avoids duplication.
        parentheses = [] # create stack for open brackets
        for i in s: # loop through input string
            if i in openBrackets:
                parentheses.append(i) # if it is an open bracket, add it to the stack
            elif i in closeBrackets:
                if not parentheses: # if it is a close bracket, and the stack is empty, must fail
                    return False
                if closeBrackets.index(i) != openBrackets.index(parentheses.pop()): # if it does match the last open bracket, fail.
                    return False
        return len(parentheses) == 0 # if the stack is empty, return true else false.
