"""
https://leetcode.com/problems/valid-anagram/
"""
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time Complexity: O(n + m), where:
            - n is the length of s 
            - m is the length of t
        Space Complexity: O(n + m)
        """
        s_maps = {}
        t_maps = {}
        for i in s:
            s_maps[i] = s_maps.get(i, 0) + 1
        for i in t:
            t_maps[i] = t_maps.get(i, 0) + 1
        return s_maps == t_maps
    

    def isAnagram_with_defaultdict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_maps = defaultdict(int)
        t_maps = defaultdict(int)

        for char in s:
            s_maps[char] += 1
        for char in t:
            t_maps[char] += 1

        return s_maps == t_maps

s = Solution()
a = s.isAnagram("success", "sscceus")
print(a)