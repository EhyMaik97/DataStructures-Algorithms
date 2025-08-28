"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_lenght = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_lenght = max(max_lenght, right-left + 1)
        
        return max_lenght
        
                
s = Solution()
a2 = s.lengthOfLongestSubstring("abcabcbb")
print(a2)