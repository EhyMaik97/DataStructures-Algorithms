"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        maps = {}
        for i, v in enumerate(numbers):
            diff =  target - v
            if diff in maps:
                return [maps[diff], i]
            maps[v] = i
                                    
s = Solution()
a = s.twoSum([2,7,11,15], 9)
a2 = s.twoSum([0,23,2,1,4,2,5,7,8,4], 28)
a3 = s.twoSum([-1,0], -1)
print(a)
print(a2)
print(a3)