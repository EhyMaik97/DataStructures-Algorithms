"""
https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
    
s = Solution()
a1 = s.containsDuplicate([6,7,8,0,1,2,2,3])
a2 = s.containsDuplicate([6,7,8,0,1,2,3])

print(a1)
print(a2)