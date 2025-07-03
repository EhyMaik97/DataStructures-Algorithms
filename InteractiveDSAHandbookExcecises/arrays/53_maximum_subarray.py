"""
https://leetcode.com/problems/maximum-subarray/
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Resolved with Kadane's Algorithm
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_sum = nums[0]
        curr_sum = nums[0]
        for n in range(1, len(nums)):
            curr_sum = max(curr_sum + nums[n], nums[n])
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
    

s = Solution()
a = s.maxSubArray([-1, 0, -4, 5, 9, -3, 2, 1, -8])
a2 = s.maxSubArray([-1, -2, 3, 5, -6, 45])
print(a)
print(a2)
            
            