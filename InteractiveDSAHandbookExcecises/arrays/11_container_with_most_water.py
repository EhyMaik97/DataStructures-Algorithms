"""
https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_contained_water = 0
        left, right = 0, len(height) - 1
        while left < right:
            base = abs(right - left)
            contained_water = base * min(height[left], height[right])
            max_contained_water = max(max_contained_water, contained_water)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return max_contained_water
    
s = Solution()
a = s.maxArea([1,8,6,2,5,4,8,3,7])
a2 = s.maxArea([1,1])

print(a)
print(a2)