"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
import unittest

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t or len(s) < len(t):
            return ""
        n = len(s)
        m = len(t)
        hash_map = {}
        for i in t:
            hash_map[i] = hash_map.get(i, 0) + 1
        left = right = 0
        count = len(hash_map)
        min_len = n+1
        min_start = 0
        while right < n:
            if s[right] in hash_map:
                hash_map[s[right]] -= 1
                if hash_map[s[right]] == 0:
                    count -= 1
            right += 1
            while count == 0:
                if right - left < min_len:
                    min_len = right - left
                    min_start = left
                if s[left] in hash_map:
                    hash_map[s[left]] += 1
                    if hash_map[s[left]] > 0:
                        count += 1
                left += 1
        if min_len == n+1:
            return ""
        return s[min_start:min_start+min_len]

 
#test solution
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_case1(self):
        str1 = "ADOBECODEBANC"
        str2 = "ABC"
        result = "BANC"
        self.assertEqual(self.s.minWindow(str1,str2),result)

    def test_case2(self):
        str1 = "a"
        str2 = "b"
        result = ""
        self.assertEqual(self.s.minWindow(str1,str2),result)

    def test_case3(self):
        str1 = "a"
        str2 = "aa"
        result = ""
        self.assertEqual(self.s.minWindow(str1,str2),result)

if __name__ == '__main__':
    unittest.main()