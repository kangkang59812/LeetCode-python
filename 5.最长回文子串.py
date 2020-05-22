#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (27.01%)
# Likes:    1270
# Dislikes: 0
# Total Accepted:    106.3K
# Total Submissions: 393.5K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"
#
#
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s is None:
            return s

        dp = [[False]*len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        start = 0
        end = 0
        maxLen = 1
        for i in range(1, len(s)):
            for j in range(0, i):
                if s[i] == s[j] and (i-j == 1 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i-j+1 > maxLen:
                        start = j
                        end = i
                        maxLen = i-j+1
        return s[start:end+1]
        # @lc code=end
