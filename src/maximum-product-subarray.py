"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

import unittest
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        maxProd = curMaxProd = curMinProd = nums[0]

        for num in nums[1:]:
            curMaxProd, curMinProd = max(num, num*curMaxProd, num*curMinProd), min(num, num*curMaxProd, num*curMinProd)
            maxProd = max(maxProd, curMaxProd)
        return maxProd

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [2,3,-2,4]
        # output
        r = 6
        self.assertEqual(Solution().maxProduct(n), r)

if __name__ == "__main__":
    unittest.main()