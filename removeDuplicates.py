"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      
        # for i, num in enumerate(nums):
        #     if num in nums[0:i]:
        #         nums[i] = "-"
        # nums.sort(key=lambda x: not isinstance(x, int))
        # return max([x for x in nums if str(x).isnumeric()])
        seen = set()
        pos = 0
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[pos] = num
                pos += 1
        return pos
