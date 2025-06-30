"""
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = len(nums)
        answer = [1] * n
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n -1, -1, -1):
            answer[i] *= right 
            right *= nums[i]
        
        return answer

s = Solution()
a = s.productExceptSelf([1,2,3,4])
print(a)