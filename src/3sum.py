"""
15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

import unittest
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time:O(n^2), Space:O(1)

        res = []
        nums.sort()
        for i in range(len(nums)-2):
            # to avoid duplicate for i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # to avoid duplicate for l
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    # to avoid duplicate for r
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [-1,0,1,2,-1,-4]
        # output
        r = [[-1,-1,2],[-1,0,1]]
        self.assertListEqual(Solution().threeSum(n), r)

if __name__ == "__main__":
    unittest.main()