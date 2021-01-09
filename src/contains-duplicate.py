"""
217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

import unittest
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    # Time: O(n), Space: O(n)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False


### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = [1,2,3,1]
        # output
        r = True
        self.assertEqual(Solution().containsDuplicate(n), r)

if __name__ == "__main__":
    unittest.main()