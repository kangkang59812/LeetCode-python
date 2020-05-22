#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.67%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 17.7K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde"
# 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#
# 若这两个字符串没有公共子序列，则返回 0。
#
#
#
# 示例 1:
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
#
#
# 示例 2:
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
#
#
# 示例 3:
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
#
#
#
#
# 提示:
#
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
#
#
#

# @lc code=start


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]   t1[1:i]  t2[1:j] 的LCS
        # n1, n2 = len(text1), len(text2)
        # dp = [[0]*(n2+1) for i in range(n1+1)]
        # for i in range(1, n1+1):
        #     for j in range(1, n2+1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[i][j] = 1+dp[i-1][j-1]
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # return dp[n1][n2]

        if not text1 or not text2:
            return 0
        n1 = len(text1)
        n2 = len(text2)
        dp = [0] * (n2+1)
        tmp = [0] * (n2+1)
        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[j] = tmp[j-1] + 1
                else:
                    dp[j] = max(tmp[j], dp[j-1])
            tmp = dp[:]  # 一起赋值要快一点
        return dp[-1]

        # n1, n2 = len(text1), len(text2)
        # pre = [0 for _ in range(n2 + 1)]
        # dp = [0 for _ in range(n2 + 1)]
        # for i in range(1,n1+1):
        #     for j in range(1, n2 + 1):
        #         if text1[i-1] == text2[j-1]:
        #             dp[j] = pre[j-1] + 1
        #         else:
        #             dp[j] = max(pre[j], dp[j-1])
        #         #这样是一个一个赋值，上面的是一起赋值
        #         pre[j-1] = dp[j-1]
        #     pre[j] = dp[j]
        # return dp[-1]
        # @lc code=end
