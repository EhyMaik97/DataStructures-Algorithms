"""
https://leetcode.com/problems/longest-repeating-character-replacement/
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        frequency_dict = defaultdict(int)
        max_freq = 0
        left = 0
        res = 0
        
        for right in range(len(s)):
            letter = s[right]
            frequency_dict[letter] += 1
            
            max_freq = max(frequency_dict.values())
            current_lenght = right - left + 1
            if current_lenght - max_freq > k:
                frequency_dict[s[left]] -= 1
                left += 1
                current_lenght = right - left + 1
            
            res = max(res, current_lenght)
        
        return res

s = Solution()
a = s.characterReplacement("AABABBA", 1)
h = s.characterReplacement("ABAAACBBBABABABAABABB", 2)
print(a)
print(h)