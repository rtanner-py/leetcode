"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""

# Initial solution involved converting list of ints to a number, incrementing by one, and then changing the int
# back into a list

# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         result = 0
#         for index, num in enumerate(digits):
#             result += num * 10**(len(digits)-(index+1))
#         return [int(i) for i in str(result+1)]

# second solution. Modfies the list in place, avoids conversion, which may be problematic with large numbers
# Only iterates until a non-9 value is found. If the 'unit' value is 8, then it only needs to look at digits[-1]
# however, if digits[-1] is a 9, then it needs to change to 0, and then look at digits[-2]

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
