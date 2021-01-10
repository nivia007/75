"""
33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order (with distinct values), and an integer target.
Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
If target is found in the array return its index, otherwise, return -1.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104
"""

import unittest
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(log n), Space: O(1)

        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [4,5,6,7,0,1,2]
        t = 3
        # output
        r = -1
        self.assertEqual(Solution().search(n, t), r)

if __name__ == "__main__":
    unittest.main()        