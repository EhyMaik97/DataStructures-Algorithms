"""
https://leetcode.com/problems/find-peak-element/
"""

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:
                # The peak is on the left
                right = mid
            else:
                # The peak is on the right
                left = mid + 1

        return left  # or right, it's the same


s = Solution()
a = s.findPeakElement([1,2,1,3,5,6,4])
print(a)