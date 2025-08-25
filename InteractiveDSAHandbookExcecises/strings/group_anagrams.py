"""
https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict

class Solution:
    def group_anagrams(self, txts: list):
        res = defaultdict(list)

        for word in txts:
            key = ''.join(sorted(word))
            res[key].append(word)

        return list(res.values())

"""------------------------------------------"""
s = Solution()
a = s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
h = s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)
print(h)