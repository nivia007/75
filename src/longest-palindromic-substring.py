"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""


import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Time: O(n^2), Space: O(n)

        longest_str = ""
        
        for idx in range(len(s)):
            longest_str = max(longest_str, self.calcPlainDrome(s, idx, idx+1), self.calcPlainDrome(s,idx,idx), key=len)
        
        return longest_str

    def calcPlainDrome(self, s: str, left: int, right: int) -> str:
        while left >- 1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1:right]

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = "cbbd"
        # output
        r = "bb"
        self.assertEqual(Solution().longestPalindrome(n), r)

if __name__ == "__main__":
    unittest.main()