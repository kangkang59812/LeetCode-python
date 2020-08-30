#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (27.24%)
# Likes:    327
# Dislikes: 0
# Total Accepted:    27.1K
# Total Submissions: 99K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#
#
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#
#
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#
#
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#
#
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false
#
#

# @lc code=start


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #   \ a b b b a
        # \ 1 0 0 0 0 0
        # a 0
        # b
        # *
        # a
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False
        s = '0'+s
        p = '0'+p
        dp = [[False]*(len(s)) for _ in range(len(p))]
        dp[0][0] = True

        for i in range(1, len(p)):
            dp[i][0] = dp[i-1][0] and p[i] == '*'
        for i in range(1, len(p)):
            for j in range(1, len(s)):
                if p[i] == '*':
                    # 匹配*对应的s中的字符及之后的  或  匹配空
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                elif p[i] == s[j] or p[i] == '?':
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
# @lc code=end
