"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] = dp[i-1][j-1] if s[i] == p[j] or p[j] == '?'
        # dp[i][j] = dp[i-1][j] or dp[i][j-1] if p[j] == '*'
        # dp[0][0] = True
        # dp[i][0] = False
        # dp[0][j] = dp[0][j-1] if p[j] == '*'
        # dp[0][j] = False if p[j] != '*'
        # return dp[-1][-1]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]
        
# test solutions
s = Solution()
assert s.isMatch("aa", "a") == False
assert s.isMatch("aa", "*") == True
assert s.isMatch("cb", "?a") == False
assert s.isMatch("adceb", "*a*b") == True
assert s.isMatch("acdcb", "a*c?b") == False