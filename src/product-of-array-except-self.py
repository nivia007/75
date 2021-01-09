"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

import unittest
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n), Space:O(n)

        output = [1]
        leftPro = 1
        rightPro = 1

        # loop from left to right (don't consider the first element)
        for i in range(1,len(nums)):
            leftPro *= nums[i-1]
            output.append(leftPro)

        # loop from right to left (don't consider the last element)        
        for j in range(len(nums)-2,-1,-1):
            rightPro *= nums[j+1]
            output[j] *= rightPro

        return output

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [1,2,3,4]
        # output
        r = [24,12,8,6]
        self.assertEqual(Solution().productExceptSelf(n), r)

if __name__ == "__main__":
    unittest.main()