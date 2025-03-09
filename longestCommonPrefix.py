"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ""
    limit = len(min(strs, key=len)) # min(strs, key=len) returns the shortest word. len() returns length
    for i in range(limit):
        letter = strs[0][i]
        for word in strs:
            if word[i] != letter: #if the letter isn't in the word, can exit as shortest common prefix found
                return prefix
        prefix += letter #letters match in all words, update prefix
    return prefix #return prefix
