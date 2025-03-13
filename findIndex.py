"""
Leet Code problem 28. Find the index of the first occurrence in a string
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

# First attempt. Runtime of 0ms, beats 100%. Memory 17.70mb, beats 81.94%.
import re
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index = re.search(needle, haystack)
        return index.span()[0] if index else -1

# Second attempt. re carries overhead, so using string.find() method. 0ms, beats 100%. Memory 17.84mb (worse)
# find(value) finds the first occurence of the specified value and returns -1 if not found. Similar to string.index() save that
# index() raises an exception if the value is not found. Problem requires we return -1 if not found, so using find().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle) #


# third attempt. Sliding window technique. Runs a window over haystack to see whether the section i:i+n == needle
# 0ms (beats 100%), memory 17.88mn (beats 33.10%). 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0
        
        for i in range(m-n+1):
            if haystack[i:i + n] == needle:
                return i
        return -1

        
