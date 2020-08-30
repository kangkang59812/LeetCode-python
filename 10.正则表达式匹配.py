#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (24.68%)
# Likes:    648
# Dislikes: 0
# Total Accepted:    29.3K
# Total Submissions: 118.9K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
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
        dp = [[False]*(len(s)+1) for _ in range(len(p)+1)]
        dp[0][0] = True
        for i in range(1, len(p)):
            dp[i+1][0] = dp[i-1][0] and p[i] == '*'
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == '*':
                    # 不需要a*和 需要1个
                    dp[i+1][j+1] = dp[i][j+1] or dp[i-1][j+1]
                    if p[i-1] == s[j] or p[i-1] == '.':
                        dp[i+1][j+1] |= dp[i+1][j]

                else:
                    dp[i+1][j+1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
        return dp[-1][-1]


# @lc code=end
