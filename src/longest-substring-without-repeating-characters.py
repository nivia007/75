"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:
Input: s = ""
Output: 0

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n), Space: O(n)
        dic = {}
        start_idx = 0
        curr_len = max_len = 0
        for idx in range(len(s)):
            if s[idx] in dic and dic[s[idx]] >= start_idx:
                start_idx = dic[s[idx]] + 1
            
            dic[s[idx]] = idx
            max_len = max(max_len, idx - start_idx + 1)
        
        return max_len

### Test
class TestSolution(unittest.TestCase):
    def test_0(self):
        # input
        n = "pwwkew"
        # output
        r = 3
        self.assertEqual(Solution().lengthOfLongestSubstring(n), r)

if __name__ == "__main__":
    unittest.main()