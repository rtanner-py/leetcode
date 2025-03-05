"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        # for pos, let in enumerate(s):
        #     value = values[let]
        #     if let == "I" and pos+1 < len(s):
        #         if s[pos+1] in ('V', 'X'):
        #             total -= value
        #             continue
        #     elif let == "X" and pos+1 < len(s):
        #         if s[pos+1] in ("L","C"):
        #             total -= value
        #             continue
        #     elif let == "C" and pos+1 < len(s):
        #         if s[pos+1] in ("D","M"):
        #             total -= value
        #             continue
        #     total += value

        # note that usually written from largest to smallest, left to right, so VI = 6, but IV = 4.
        # if you go right to left (reversed(s)) then: if you hit a character that is smaller than the previous, you need to subtract; otherwise you add:

        # previous_value = 0
        # for letter in reversed(s):
        #     value = values[letter]
        #     if value < previous_value:
        #         total -= value
        #     else:
        #         total += value
        #     previous_value = value
        # return total

        #if we know we are starting with the last character, then why initialise total  at 0, rather than the value of the last char?
        total = values[s[-1]]
        previous_value = total

        #instead of using a for loop, use an index and traverse the string in reverse. We already have the last letter, so start at the second to last
        for i in range(len(s) - 2, -1, -1):
            value = values[s[i]]
            total += -value if value < previous_value else value
            previous_total = value
        return total


