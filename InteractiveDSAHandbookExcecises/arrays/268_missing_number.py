"""
https://leetcode.com/problems/missing-number/
Difficulty: Easy
"""

class Solution:
    def missing_number_arithmetic_sum(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        real_total_sum = (len(nums) * (len(nums)+1)) // 2
        nums_sum = 0
        for _ in nums:
            nums_sum += _
        
        return real_total_sum - nums_sum
    
    def missing_number_hashset(self, nums: list[int]) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        hashset = set(nums)
        
        for n in range(len(nums)+1): # len(nums)+1 cause we know that in the list is
                                     # missing one number, se we need to check everyone
            if n not in hashset:
                return n
        
    
"""------------------------------------------"""
s = Solution()
a = s.missing_number_arithmetic_sum([3,4,0,1,2,5,6,9,7])
h = s.missing_number_hashset([3,4,0,1,2,5,6,9,7])
print(h)