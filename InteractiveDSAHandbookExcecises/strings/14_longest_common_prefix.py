"""
https://leetcode.com/problems/longest-common-prefix/
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Time complexity: O(m * n)
        """
        prefix = strs[0]
        pref_len = len(prefix)
        
        for s in strs[1:]:
            while prefix != s[0:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                prefix = prefix[0:pref_len]
        return prefix
    
s = Solution()
a = s.longestCommonPrefix(["flower", "flow", "flooting", "flight"])
h = s.longestCommonPrefix(["eat", "bat", "school"])
print(a)
print(h)
    